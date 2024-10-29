from django.db import models
from encrypted_model_fields.fields import EncryptedCharField, EncryptedEmailField


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    encrypted_ssn = EncryptedCharField(max_length=11)
    encrypted_email = EncryptedEmailField()
