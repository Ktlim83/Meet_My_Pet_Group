from django.db import models
from login.models import *
from django.core.files.storage import FileSystemStorage
from datetime import date



class PostManager(models.Manager):

    def validate(self, post_data):
        errors = {}
        #title cannot be empty.
        if len(post_data['title']) < 1:
            errors['title'] = "Title cannot be empty."
        #content must contain at least 5 characters.
        if len(post_data['content']) < 5:
            errors['content'] = "Content must contain at lease 5 characters."

        return errors
# Post Information
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    likes = models.ManyToManyField(User, related_name="post_like")

    def num_of_likes(self):
        return self.likes.count()

    objects = PostManager()

class Comment(models.Model):
    content = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
    message = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    