from django.db.models import Count, Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from courses.models import Course, CourseComment
from courses.serializers import CourseSerializer, CourseDetailSerializer, CourseCommentSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'degree', 'rating']
    search_fields = ['title']


class CourseDetailAIView(generics.RetrieveAPIView):
    serializer_class = CourseDetailSerializer

    def get_queryset(self):
        queryset = Course.objects.annotate(count_chapters=Count('chapters'),
                                           count_lessons=Count('chapters__lessons'))
        return queryset


class CourseCommentAPIView(generics.ListAPIView):
    queryset = CourseComment
    serializer_class = CourseCommentSerializer

    def get_queryset(self):
        course_id = self.kwargs['pk']
        queryset = CourseComment.objects.filter(course_id=course_id)
        return queryset
