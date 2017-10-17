from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Course,Lesson,Comment
from .serializers import CourseSerializer,LessonSerializer,CommentSerializer

class CourseList(generics.GenericAPIView):
    
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        pass