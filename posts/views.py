from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import AllPostSerializers, LikeSerializers
from .models import Post, Like
from django.contrib.auth import authenticate, login
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


# Create your views here.
class ListPosts(APIView):
    def get(self, request, format=None):
        postModel = Post.objects.all()
        postsJson = AllPostSerializers(postModel, many=True)
        return Response(postsJson.data)


class PostLikeView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LikeSerializers

    @swagger_auto_schema(request_body=LikeSerializers)
    
    def post(self, request, format=None):
        like_id = request.data['like_id']
        like_filter = Like.objects.filter(post__post_id=like_id).first()
        if request.user in like_filter.users.filter(requirement_comment_likes=request.user.id):
            like_filter.users.remove(request.user.id)
            return Response("User Added Like",status=status.HTTP_200_OK)
        else:
            current_user = request.user
            like_filter.users.add(current_user)
            return Response("User Removed Like",status=status.HTTP_200_OK)
        
    def get(self, request, format=None):
        user = authenticate(request, username="sampleuser", password="sample@123")
        if user is not None:
            login(request, user)
            print("done")
        else:
            print("nothing done")
        if request.user.is_authenticated:
            print("authenticated")
        else:
            print("not auth")
        return Response("user auth")
