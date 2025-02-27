from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class  User(AbstractUser):
    avatar = models.ImageField(
        upload_to = 'avatars/',
        blank=True, null=True
    )
    favorite_movies = models.ManyToManyField('apple_tv.Movie')