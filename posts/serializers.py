from rest_framework import serializers
from .models import Post, Like


class AllPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ("post", "users")
