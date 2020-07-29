from django.contrib import admin
from graphQL import models


# Register your models here.
class TrackAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'url', 'created_at']
    ordering = ['id']


admin.site.register(models.Track, TrackAdmin)
