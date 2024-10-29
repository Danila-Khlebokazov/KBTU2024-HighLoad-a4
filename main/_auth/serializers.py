from rest_framework import serializers
from django.contrib.auth.models import User
from .models import UserProfile
from django.db import transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        with transaction.atomic():
            user = User(
                username=validated_data['username'],
                email=validated_data['email']
            )
            user.set_password(validated_data['password'])
            user.save()
            user_profile = UserProfile(user=user, encrypted_ssn='123456789', encrypted_email=user.email)
            user_profile.save()
        return user
