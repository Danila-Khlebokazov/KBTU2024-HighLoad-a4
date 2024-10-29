import csv

from celery import shared_task
from django.conf import settings
from django.core.files.storage import default_storage

from datas.models import TradeIndex, Upload


@shared_task
def process_csv_data(upload_id):
    upload = Upload.objects.get(id=upload_id)
    with open(default_storage.path(upload.file.path), 'r') as file:
        reader = csv.DictReader(file)
        batch = []
        for row in reader:
            trade_index = TradeIndex(
                series_reference=row['Series_reference'],
                period=row['Period'],
                data_value=row.get('Data_value', None) or 0,
                status=row['STATUS'],
                units=row['UNITS'],
                magnitude=int(row['MAGNTUDE']),
                subject=row['Subject'],
                group=row['Group'],
                series_title_1=row['Series_title_1'],
                series_title_2=row['Series_title_2'],
                series_title_3=row['Series_title_3'],
            )
            batch.append(trade_index)

            if len(batch) == settings.UPLOAD_BATCH_SIZE:
                TradeIndex.objects.bulk_create(batch)
                batch.clear()

        if batch:
            TradeIndex.objects.bulk_create(batch)

    upload.status = "Finished"
    upload.save()
