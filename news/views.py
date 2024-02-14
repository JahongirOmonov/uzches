from news.models import New, SocialApps, UsingRules
from news.serializers import NewsSerializer, SocialAppsSerializer, UsingRulesSerializer
from rest_framework import generics
from rest_framework import filters


class NewListAPIView(generics.ListAPIView):
    queryset = New.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'short_description']


class SocialAppsListAPIView(generics.ListAPIView):
    queryset = SocialApps.objects.all()
    serializer_class = SocialAppsSerializer


class UsingRulesListAPIView(generics.ListAPIView):
    queryset = UsingRules.objects.all()
    serializer_class = UsingRulesSerializer
