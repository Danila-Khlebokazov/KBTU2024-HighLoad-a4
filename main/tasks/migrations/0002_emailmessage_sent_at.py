# Generated by Django 5.1.2 on 2024-10-28 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailmessage',
            name='sent_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
