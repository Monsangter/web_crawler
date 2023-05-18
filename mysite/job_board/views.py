from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Wanted, Jobkorea, Saramin
from .serializers import WantedSerializer, JobkoreaSerializer, SaraminSerializer

class PagePagination(PageNumberPagination):
    page_size = 20

class JobListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        paginator = PagePagination()
        job_type = request.query_params.get('type')

        if job_type == 'wanted':
            queryset = Wanted.objects.all().order_by('-created_at')
            serializer_class = WantedSerializer
        elif job_type == 'jobkorea':
            queryset = Jobkorea.objects.all().order_by('-created_at')
            serializer_class = JobkoreaSerializer
        elif job_type == 'saramin':
            queryset = Saramin.objects.all().order_by('-created_at')
            serializer_class = SaraminSerializer
        else:
            return Response({"error": "Invalid type parameter"}, status=400)

        context = paginator.paginate_queryset(queryset, request)
        serializer = serializer_class(context, many=True)

        return paginator.get_paginated_response(serializer.data)
