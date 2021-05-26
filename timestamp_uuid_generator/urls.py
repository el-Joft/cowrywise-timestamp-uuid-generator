from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from timestamp_uuid_generator import views

urlpatterns = [
    path('generate_uuid/', views.UUIDTimestampView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)