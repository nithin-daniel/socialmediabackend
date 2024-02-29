from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import AllPostSerializers,LikeSerializers
from .models import Post,Like
from django.contrib.auth import authenticate, login
# Create your views here.
class ListPosts(APIView):
    def get(self,request,format=None):
        postModel = Post.objects.all()
        postsJson = AllPostSerializers(postModel,many=True)
        return Response(postsJson.data)
    
class PostLikeView(APIView):
    permission_classes = [AllowAny]
    def get(self,request,format=None):
        print(request.user)
        like_id = request.data['like_id']
        like_model = Like.objects.filter(post=like_id)
        like_serializer = LikeSerializers(like_model,many=True)

        # hello = Like.objects.all()
        # print(hello.Users.user)
        print(like_model.users.add(request.user))


        '''For a test purpose done this authentication method'''

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