from django.contrib import admin
from .models import Tip, Achievement,UserAchievement


@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display  = ('title', 'order')
    list_editable = ('order',)
    search_fields = ('title',)

@admin.register(UserAchievement)
class UserAchievementAdmin(admin.ModelAdmin):
    list_display = ('user', 'achievement', 'completed', 'awarded_at')
    list_filter  = ('completed', 'awarded_at')
    search_fields = ('user__username', 'achievement__title')
