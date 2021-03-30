from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=128)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    img = models.ImageField(upload_to='recipe_images')
    date = models.DateField(default=datetime.now)
    text = models.TextField()
    tags = TaggableManager()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.TextField(default="", blank=True)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(default=datetime.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}: {self.text}"
