from django.urls import path
from .views import CombinedListAPIView

urlpatterns = [
    path('jobs/', CombinedListAPIView.as_view(), name='combined-list'),
]