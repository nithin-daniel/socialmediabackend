from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AllPostSerializers
from .models import Post
# Create your views here.
class ListPosts(APIView):
    def get(self,request,format=None):
        # usernames = [post.post_author for post in AllPostSerializers.objects.all()]
        post = Post.objects.all()
        usernames = AllPostSerializers(post,many=True)
        return Response(usernames.data)