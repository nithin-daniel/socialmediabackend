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
        # like_id = request.data['like_id']
        # like_filter = Like.objects.filter(post__post_id=like_id)
        # like_user_filter = like_filter.get(users=request.user)
        # if like_user_filter:
        #     if like_user_filter.users.exists():
        #         like_user_filter.users.remove(request.user)
        #         return Response("User removed", status=status.HTTP_201_CREATED)
        #     else:
        #         like_user_filter.users.add(request.user)
        #         return Response("User added", status=status.HTTP_201_CREATED)
        # else:
        #     print("not found")


        # try:
        #     like_id = request.data['like_id']
        #     like_filter = Like.objects.filter(post__post_id=like_id)
        #     like_user_filter = like_filter.get(users=request.user)

        #     if like_user_filter.users:
        #         like_user_filter.users.remove(request.user)
        #         return Response("User removed", status=status.HTTP_201_CREATED)
        #     else:
        #         like_user_filter.users.add(request.user)
        # except Like.DoesNotExist:
        #     return Response("User not liked", status=status.HTTP_201_CREATED)   


        like_id = request.data['like_id']
        like_filter = Like.objects.filter(post__post_id=like_id).first()
        if request.user in like_filter.users.filter(requirement_comment_likes=request.user.id):
            like_filter.users.remove(request.user.id)
        else:
            current_user = request.user
            like_filter.users.add(current_user)


        # like_filter = Like.objects.filter(post__post_id=like_id).first()
        # print(like_filter)
        # like_user_filter = like_filter.get(users=request.user)
        # if request.user in like_user_filter:
        #     like_filter.users.remove(request.user)
        #     print("fund")
        # else:
        #     like_filter.users.add(request.user)
        #     print(like_filter.users)
        #     print("not fund")
        return Response("user dummy")
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
    #     print(request.user)
    #     like_id = request.data['like_id']
    #     like_model = Like.objects.filter(post=like_id)
    #     like_serializer = LikeSerializers(like_model, many=True)
        #   print(request.auth)
    #     # hello = Like.objects.all()
    #     # print(hello.Users.user)
    #     print(like_model.users.add(request.user))

    #     """For a test purpose done this authentication method"""

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

    #     # if request.user in like_serializer.data[0]['users']:
    #     #     like_model.users.remove(request.user)
    #     #     return Response("user removed")
    #     # else:
    #     #     like_model.users.add(request.user)
        return Response("user added")
