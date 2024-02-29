from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AllPostSerializers,LikeSerializers
from .models import Post,Like
# Create your views here.
class ListPosts(APIView):
    def get(self,request,format=None):
        postModel = Post.objects.all()
        postsJson = AllPostSerializers(postModel,many=True)
        return Response(postsJson.data)
    
class PostLikeView(APIView):
    def post(self,request,format=None):
        like_id = request.data['like_id']
        like_model = Like.objects.filter(post=like_id)
        like_serializer = LikeSerializers(like_model,many=True)
        if request.user in like_serializer.data[0]['users']:
            like_model.users.remove(request.user)
            return Response(like_serializer.data[0]['users'])
        else:
            like_model.users.add(request.user)
            return Response("user removed")