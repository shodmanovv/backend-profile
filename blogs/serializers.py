from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    created_format = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'categorys', 'name', 'img', 'img2', 'text', 'text2', 'created']
        ordering = ('-created',)

    def get_created_format(self, obj):
        return obj.created.strftime('%b %d %Y')

    def __str__(self):
        return self.name
