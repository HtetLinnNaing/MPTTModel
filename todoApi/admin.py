from django.contrib import admin
from todoApi.models import todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'done', 'created_at']

admin.site.register(todo, TodoAdmin)
