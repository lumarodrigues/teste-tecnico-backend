from django.urls import path
from .views import DocumentAPIView

urlpatterns = [
    path('documents/', DocumentAPIView.as_view(), name='documents'),
]
