from django.utils.decorators import method_decorator
from django.http import JsonResponse

from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from drf_yasg.utils import swagger_auto_schema

from .serializers import (
    NewsSerializer
)

from .models import (
    News
)

def home(request):
    return JsonResponse(
    	data={
	        "docs_url": "https://drf-generator-swagger.vercel.app/docs/"
	    }
    )


@method_decorator(name="get", decorator=swagger_auto_schema(tags=['News']))
class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@method_decorator(name="post", decorator=swagger_auto_schema(tags=['News']))
class NewsCreateAPIView(CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    parser_classes = [MultiPartParser]


@method_decorator(name="get", decorator=swagger_auto_schema(tags=['News']))
class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


@method_decorator(name="put", decorator=swagger_auto_schema(tags=['News']))
@method_decorator(name="patch", decorator=swagger_auto_schema(tags=['News']))
class NewsUpdateAPIView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    parser_classes =  [MultiPartParser]

@method_decorator(name="delete", decorator=swagger_auto_schema(tags=['News']))
class NewsDeleteAPIView(DestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer