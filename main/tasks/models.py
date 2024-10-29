from django.db import models


class EmailMessage(models.Model):
    recipient = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    body = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)
