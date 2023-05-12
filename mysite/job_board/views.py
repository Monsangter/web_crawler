# views.py
from django.db.models import Q
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Wanted, Jobkorea, Saramin
from .serializers import WantedSerializer, JobkoreaSerializer, SaraminSerializer

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class CombinedListAPIView(generics.ListAPIView):
    serializer_class = None
    pagination_class = CustomPagination

    def get_queryset(self):
        model = self.request.query_params.get('model', 'wanted')
        search = self.request.query_params.get('search', '')

        if model == 'jobkorea':
            queryset = Jobkorea.objects.filter(Q(company__icontains=search) | Q(detail__icontains=search))
            self.serializer_class = JobkoreaSerializer
        elif model == 'saramin':
            queryset = Saramin.objects.filter(Q(company__icontains=search) | Q(detail__icontains=search))
            self.serializer_class = SaraminSerializer
        else:
            queryset = Wanted.objects.filter(Q(company__icontains=search) | Q(position__icontains=search))
            self.serializer_class = WantedSerializer

        return queryset