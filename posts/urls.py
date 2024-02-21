from django.urls import path
from .views import ListPosts
urlpatterns = [
    path('',ListPosts.as_view())
]
