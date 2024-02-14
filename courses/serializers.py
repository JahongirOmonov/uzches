from django.contrib.auth.models import User
from rest_framework import serializers
from courses.models import Course, CourseComment


class CourseSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(source='category.title')

    class Meta:
        model = Course
        fields = (
            'title', 'author', 'image', 'price_discount', 'price', 'degree', 'category', 'rating', 'like')


class CourseDetailSerializer(serializers.ModelSerializer):
    count_chapters = serializers.IntegerField()
    count_lessons = serializers.IntegerField()

    class Meta:
        model = Course
        fields = ('title', 'price', 'price_discount', 'degree', 'rating', 'like', 'count_chapters', 'count_lessons')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class CourseCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course = serializers.StringRelatedField(source='course.title')

    class Meta:
        model = CourseComment
        fields = ('course', 'user', 'rating', 'description', 'created_at', 'updated_at')
