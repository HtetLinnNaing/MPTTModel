from django.contrib import admin
from product.models import Category
from mptt.admin import DraggableMPTTAdmin


# Register your models here.
class CategoryInline(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'description', 'status','create_at')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryInline)
