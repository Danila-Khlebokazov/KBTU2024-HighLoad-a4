from .views import upload_csv_view, get_upload_status
from django.urls import path

urlpatterns = [
    path('upload', upload_csv_view),
    path('status/<int:upload_id>', get_upload_status),
]
