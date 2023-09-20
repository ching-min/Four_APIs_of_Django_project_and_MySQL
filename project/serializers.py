from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .model import Articles
import json
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Articles
        fields = ["date", "title", "content", "tags"]