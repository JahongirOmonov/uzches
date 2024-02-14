from django.db import models

from common.utils import BaseModel


class New(BaseModel):
    title = models.CharField(max_length=256)
    image = models.ImageField(upload_to='photos/')
    short_description = models.TextField()
    description = models.TextField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class SocialApps(BaseModel):
    instagram_url = models.CharField(max_length=128, null=True, blank=True)
    telegram_url = models.CharField(max_length=128, null=True, blank=True)
    youtube_url = models.CharField(max_length=128, null=True, blank=True)
    twitter_url = models.CharField(max_length=128, null=True, blank=True)
    facebook_url = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return f"Social app url"


class UsingRules(BaseModel):
    description = models.TextField()

    def __str__(self):
        return f"None"
