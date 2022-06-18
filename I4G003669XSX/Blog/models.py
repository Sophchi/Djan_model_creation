from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Post(models.Model):
    Title  = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    Created_date = models.DateTimeField(auto_created=True)
    Published_date = models.DateTimeField(auto_now_add=True)


# whenever this model is updated. always perform two python functions; makemigrations and migrate dont forget.