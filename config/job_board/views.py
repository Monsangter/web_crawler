from rest_framework import viewsets
from .models import Wanted, Jobkorea, Saramin
from .serializers import WantedSerializer, JobkoreaSerializer, SaraminSerializer

class WantedViewSet(viewsets.ModelViewSet):
    queryset = Wanted.objects.all()
    serializer_class = WantedSerializer

class JobkoreaViewSet(viewsets.ModelViewSet):
    queryset = Jobkorea.objects.all()
    serializer_class = JobkoreaSerializer

class SaraminViewSet(viewsets.ModelViewSet):
    queryset = Saramin.objects.all()
    serializer_class = SaraminSerializer
    
