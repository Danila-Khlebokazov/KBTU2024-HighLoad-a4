from django.db import models
from django.contrib.auth.models import User


class Upload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')


class TradeIndex(models.Model):
    series_reference = models.CharField(max_length=50)
    period = models.CharField(max_length=100)
    data_value = models.DecimalField(max_digits=20, decimal_places=5)
    status = models.CharField(max_length=100)
    units = models.CharField(max_length=20)
    magnitude = models.IntegerField()
    subject = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    series_title_1 = models.CharField(max_length=100)
    series_title_2 = models.CharField(max_length=100)
    series_title_3 = models.CharField(max_length=100)
