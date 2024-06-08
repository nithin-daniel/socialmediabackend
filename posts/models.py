from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
"""
post_id 
post_author
post_title
post_description
post_posted_date
post_last_updated_date
post_uploaded_time
post_last_uploaded_time
post_image_link

# Make another model for this
post_like
post_dislike


"""


class Post(models.Model):
    post_id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    # post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=300)
    post_description = models.TextField()
    post_posted_date = models.DateField(auto_now_add=True)
    post_last_updated_date = models.DateField(auto_now=True)
    post_uploaded_time = models.TimeField(auto_now_add=True)
    post_last_uploaded_time = models.TimeField(auto_now=True)
    post_image_link = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.post_id)


class Like(models.Model):
    """like  Post"""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name="requirement_comment_likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.post.post_id)
