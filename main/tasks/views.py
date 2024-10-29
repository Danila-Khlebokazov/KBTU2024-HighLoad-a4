from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from _auth.permissions import NoAdminPermission
from .formas import SendAsyncEmailForm
from .models import EmailMessage
from .services import send_email_message
from .tasks import send_email_message_task


@api_view(["POST"])
def send_test_email(request):
    message = EmailMessage.objects.create(
        recipient=request.user,
        subject="Test Email",
        body="This is a test email message."
    )

    send_email_message(message)

    return Response("ok")


@api_view(["POST"])
@permission_classes([NoAdminPermission])
def send_async_email(request):
    form = SendAsyncEmailForm(request.data)
    if form.is_valid():
        recipient = get_object_or_404(User, email=form.cleaned_data["send_to"])

        message = EmailMessage.objects.create(
            recipient=recipient,
            subject=form.cleaned_data["subject"],
            body=form.cleaned_data["body"]
        )

        send_email_message_task.delay(message_id=message.id)

        return Response({"message": "Email is being sent."}, status=status.HTTP_200_OK)

    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
