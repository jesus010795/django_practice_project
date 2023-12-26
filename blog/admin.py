from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated',)
    list_filter = ('categories','author__username',)
    list_display = ('title', 'author', 'published','post_categories')
    ordering = ('author', 'published',)
    date_hierarchy = 'published'
    search_fields = ('title', 'author__username',)

    def post_categories(self, obj):
        return ', '.join([category.name for category in obj.categories.all().order_by('name')])
    
    post_categories.short_description = 'categorias'

admin.site.register(Category, CategryAdmin)
admin.site.register(Post, PostAdmin)
