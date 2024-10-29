from django.core.files.storage import default_storage
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from datas.models import Upload
from .forms import UploadForm
from .models import Upload
from .tasks import process_csv_data


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload_csv_view(request):
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        upload = Upload.objects.create(
            user=request.user,
            file=form.cleaned_data['file']
        )

        process_csv_data.delay(upload.id)

        return Response({'status': 'success', "id": upload.id}, status=200)

    return Response({'status': 'no file'}, status=400)


@api_view(['GET'])
def get_upload_status(request, upload_id):
    upload = get_object_or_404(Upload, id=upload_id)
    return Response({'status': upload.status, 'file': upload.file}, status=200)
