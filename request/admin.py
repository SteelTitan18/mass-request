from django.contrib import admin
from .models import Announcement
from .models import Church
from .models import ChurchRequest
from .models import Suggestion


# Register your models here.

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_filter = ['title', 'announcement_church']


@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    list_filter = ['name', 'status']


@admin.register(ChurchRequest)
class ChurchRequestAdmin(admin.ModelAdmin):
    list_filter = ['customer', 'status', 'created', 'request_church']


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_filter = ['created', 'updated', 'suggestion_church']
