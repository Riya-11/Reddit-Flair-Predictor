from rest_framework import serializers
from .models import *


class RedditPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedditPost
        fields = ['upload_file']
