from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Course,Lesson,Comment
from .serializers import CourseListSerializer,LessonSerializer,CommentSerializer
from RestApi.response import RestResponse,ResponseStatus

class CourseList(generics.GenericAPIView):
    
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response = self.get_paginated_response(serializer.data)
            return RestResponse(data=response.data,status=ResponseStatus.OK)

        serializer = self.get_serializer(queryset, many=True)
        
        return RestResponse(data=serializer.data,status=ResponseStatus.OK)
