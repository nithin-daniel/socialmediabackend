from django.urls import path
from .views import ListPosts, PostLikeView

urlpatterns = [
    path("", ListPosts.as_view()),
    path("like/", PostLikeView.as_view()),
]
