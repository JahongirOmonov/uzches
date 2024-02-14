from django.urls import path
from news.views import NewListAPIView, SocialAppsListAPIView, UsingRulesListAPIView
urlpatterns = [
    path('', NewListAPIView.as_view()),
    path('social/', SocialAppsListAPIView.as_view()),
    path('rules/', UsingRulesListAPIView.as_view()),
]