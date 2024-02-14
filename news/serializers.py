from rest_framework import serializers
from news.models import New, SocialApps, UsingRules


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ('id', 'title', 'image', 'short_description', 'description', 'views', 'created_at', 'updated_at')


class SocialAppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialApps
        fields = ('instagram_url', 'telegram_url', 'youtube_url', 'twitter_url', 'facebook_url')


class UsingRulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsingRules
        fields = ('description', )
