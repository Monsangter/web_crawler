from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Wanted, Jobkorea, Saramin
from .serializers import WantedSerializer, JobkoreaSerializer, SaraminSerializer
from django.views.generic import TemplateView

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class WantedListAPIView(APIView):
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        queryset = Wanted.objects.all().order_by('-created_at')
        page = self.pagination_class().paginate_queryset(queryset, request)
        serializer = WantedSerializer(page, many=True)
        return Response(serializer.data)

class JobkoreaListAPIView(APIView):
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        queryset = Jobkorea.objects.all().order_by('-created_at')
        page = self.pagination_class().paginate_queryset(queryset, request)
        serializer = JobkoreaSerializer(page, many=True)
        return Response(serializer.data)

class SaraminListAPIView(APIView):
    pagination_class = CustomPagination

    def get(self, request, *args, **kwargs):
        queryset = Saramin.objects.all().order_by('-created_at')
        page = self.pagination_class().paginate_queryset(queryset, request)
        serializer = SaraminSerializer(page, many=True)
        return Response(serializer.data)

class JobBoardTemplateView(TemplateView):
    template_name = "frontend/index.html"