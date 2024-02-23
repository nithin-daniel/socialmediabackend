from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AllPostSerializers
from .models import Post
# Create your views here.
class ListPosts(APIView):
    def get(self,request,format=None):
        postModel = Post.objects.all()
        postsJson = AllPostSerializers(postModel,many=True)
        return Response(postsJson.data)