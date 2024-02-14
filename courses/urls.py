from django.urls import path

from courses.views import CourseListAPIView, CourseDetailAIView, CourseCommentAPIView

urlpatterns = [
    path('', CourseListAPIView.as_view()),
    path('course-detail/<int:pk>/', CourseDetailAIView.as_view()),
    path('course-comments/<int:pk>/', CourseCommentAPIView.as_view()),
]
