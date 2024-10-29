from tasks.views import send_test_email, send_async_email
from django.urls import path

urlpatterns = [
    path('', send_test_email),
    path('async', send_async_email),
]
