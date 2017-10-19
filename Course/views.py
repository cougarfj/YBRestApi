from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Course,Lesson,Comment,Advertisement
from .serializers import CourseListSerializer,CourseDetailSerializer,LessonSerializer,CommentSerializer,AdvertisementSerializer
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


class CourseDetail(generics.GenericAPIView):
    
    queryset = None
    serializer_class = CourseDetailSerializer

    def get(self, request, *args, **kwargs):

        data = request.query_params
        course_id = data.get('course_id')

        if course_id == None:
            return RestResponse(data=None, status=ResponseStatus.PARAMS_ERROR, detail='argument[course_id] is required')
        else:
            self.queryset = Course.objects.get(id=course_id)
            serializer = self.get_serializer(self.queryset)
            return RestResponse(data=serializer.data,status=ResponseStatus.OK)


class RecommendCourseList(generics.GenericAPIView):
    queryset = Course.objects.filter(is_recommend=True)[:4]
    serializer_class = CourseListSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return RestResponse(data=serializer.data,status=ResponseStatus.OK)

class AdList(generics.GenericAPIView):
    queryset = Advertisement.objects.filter(is_show=True)
    serializer_class = AdvertisementSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return RestResponse(data=serializer.data,status=ResponseStatus.OK)