from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from .models import Movie, Category, Tag, Reaction, Comment

def home_view(request):
    qs = Movie.objects.filter(status='published').order_by('-created_at')
    categories = Category.objects.annotate(total=Count('movies'))
    return render(request, 'movies/home.html', {'movies': qs, 'categories': categories})

def movie_detail(request, slug):
    movie = get_object_or_404(Movie, slug=slug, status='published')
    likes = movie.reactions.filter(value='like').count()
    dislikes = movie.reactions.filter(value='dislike').count()
    comments = movie.comments.filter(is_approved=True).order_by('-created_at')
    saved = watched = False
    if request.user.is_authenticated:
        profile = request.user.profile
        saved = movie in profile.saved_movies.all()
        watched = movie in profile.watched_movies.all()
    return render(request, 'movies/detail.html', {
        'movie': movie, 'likes': likes, 'dislikes': dislikes,
        'comments': comments, 'saved': saved, 'watched': watched
    })

def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    qs = category.movies.filter(status='published').order_by('-created_at')
    return render(request, 'movies/category.html', {'category': category, 'movies': qs})

def search_view(request):
    q = request.GET.get('q', '')
    tag = request.GET.get('tag')
    cat = request.GET.get('cat')
    qs = Movie.objects.filter(status='published')
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(description__icontains=q))
    if tag:
        qs = qs.filter(tags__slug=tag)
    if cat:
        qs = qs.filter(category__slug=cat)
    qs = qs.distinct().order_by('-created_at')
    return render(request, 'movies/search.html', {'movies': qs, 'q': q})

@login_required
def toggle_save(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id, status='published')
    profile = request.user.profile
    if movie in profile.saved_movies.all():
        profile.saved_movies.remove(movie)
    else:
        profile.saved_movies.add(movie)
    return redirect('movies:detail', slug=movie.slug)

@login_required
def toggle_watched(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id, status='published')
    profile = request.user.profile
    if movie in profile.watched_movies.all():
        profile.watched_movies.remove(movie)
    else:
        profile.watched_movies.add(movie)
    return redirect('movies:detail', slug=movie.slug)

@login_required
def react_view(request, movie_id, value):
    movie = get_object_or_404(Movie, id=movie_id, status='published')
    if value not in ('like', 'dislike'):
        return redirect('movies:detail', slug=movie.slug)
    reaction, created = Reaction.objects.get_or_create(user=request.user, movie=movie, defaults={'value': value})
    if not created:
        reaction.value = value
        reaction.save()
    return redirect('movies:detail', slug=movie.slug)

@login_required
def comment_view(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id, status='published')
    body = request.POST.get('body', '').strip()
    if body:
        Comment.objects.create(user=request.user, movie=movie, body=body)
    return redirect('movies:detail', slug=movie.slug)
