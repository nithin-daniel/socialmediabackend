from django.urls import path
from .views import ListPosts, PostLikeView,PostAddView

urlpatterns = [
    path("", ListPosts.as_view()),
    path("add/", PostAddView.as_view()),
    path("like/", PostLikeView.as_view()),
]
