from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Extra', {'fields': ('display_name', 'avatar', 'bio')}),
    )
    list_display = ('username', 'email', 'display_name', 'is_staff', 'date_joined')
    search_fields = ('username', 'email', 'display_name')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    filter_horizontal = ('saved_movies', 'watched_movies')



