from django.urls import path
from .views import WantedListAPIView, JobkoreaListAPIView, SaraminListAPIView, JobBoardTemplateView


urlpatterns = [
    path('', JobBoardTemplateView.as_view(), name='job_board'),
    path('job_board/wanted', WantedListAPIView.as_view(), name='wanted-list'),
    path('job_board/jobkorea', JobkoreaListAPIView.as_view(), name='jobkorea-list'),
    path('job_board/saramin', SaraminListAPIView.as_view(), name='saramin-list'),
]