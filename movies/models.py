from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=80, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Movie(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [(DRAFT, 'Draft'), (PUBLISHED, 'Published')]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    video_file = models.FileField(upload_to='videos/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='movies')
    tags = models.ManyToManyField(Tag, blank=True, related_name='movies')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=DRAFT)
    release_year = models.PositiveIntegerField(blank=True, null=True)
    duration_min = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Reaction(models.Model):
    LIKE = 'like'
    DISLIKE = 'dislike'
    CHOICES = [(LIKE, 'Like'), (DISLIKE, 'Dislike')]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reactions')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reactions')
    value = models.CharField(max_length=7, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f'{self.user} -> {self.movie} ({self.value})'

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.movie}'
