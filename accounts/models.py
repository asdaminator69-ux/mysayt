from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
class User(AbstractUser):
    display_name = models.CharField(max_length=150, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.display_name or self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    saved_movies = models.ManyToManyField('movies.Movie', blank=True, related_name='saved_by')
    watched_movies = models.ManyToManyField('movies.Movie', blank=True, related_name='watched_by')

    def __str__(self):
        return f"Profile({self.user})"


