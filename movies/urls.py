from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('movie/<slug:slug>/', views.movie_detail, name='detail'),
    path('category/<slug:slug>/', views.category_list, name='category'),
    path('search/', views.search_view, name='search'),
    path('toggle-save/<int:movie_id>/', views.toggle_save, name='toggle_save'),
    path('toggle-watched/<int:movie_id>/', views.toggle_watched, name='toggle_watched'),
    path('react/<int:movie_id>/<str:value>/', views.react_view, name='react'),
    path('comment/<int:movie_id>/', views.comment_view, name='comment'),
]
