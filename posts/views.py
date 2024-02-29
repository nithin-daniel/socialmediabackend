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
        # users = User.objects.filter(id__in=request.data.get("users"))
        # post = Post.objects.get(post_id=request.data.get("post"))
        # data = {"post": post, "users": users}

        serializer = LikeSerializers(data=request.data)
        # serializer.save()

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        print(request.user)
        # like_id = request.data['like_id']
        like_model = Like.objects.filter(post=like_id)
        like_serializer = LikeSerializers(like_model, many=True)

        # hello = Like.objects.all()
        # print(hello.Users.user)
        print(like_model.users.add(request.user))

        """For a test purpose done this authentication method"""

        # user = authenticate(request, username="sampleuser", password="sample@123")
        # if user is not None:
        #     login(request, user)
        #     print("done")
        # else:
        #     print("nothing done")
        # if request.user.is_authenticated:
        #     print("authenticated")
        # else:
        #     print("not auth")

        # if request.user in like_serializer.data[0]['users']:
        #     like_model.users.remove(request.user)
        #     return Response("user removed")
        # else:
        #     like_model.users.add(request.user)
        # return Response("user added")
        return Response("user added")
