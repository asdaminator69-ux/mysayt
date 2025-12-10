from django.contrib import admin
from .models import Movie, Category, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'release_year', 'created_at')
    list_filter = ('status', 'category', 'release_year')
    search_fields = ('title', 'description')
    prepopulated_fields = {"slug": ("title",)}

    fieldsets = (
        ('Asosiy ma’lumotlar', {
            'fields': ('title', 'slug', 'description', 'poster', 'video_file')
        }),
        ('Klassifikatsiya', {
            'fields': ('category', 'tags')
        }),
        ('Holat va qo‘shimcha', {
            'fields': ('status', 'release_year', 'duration_min')
        }),
    )

