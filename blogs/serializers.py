from rest_framework import serializers
from .models import Post
from django.db import models
from datetime import datetime

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'categorys', 'name', 'img', 'img2', 'text', 'text2', 'created']
        ordering = ('-created',)

    @property   
    def created_format(self):
        return self.created.strftime('%b %d %Y')

    def __str__(self) -> str:
        return self.name