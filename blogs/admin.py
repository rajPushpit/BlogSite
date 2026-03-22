from django.contrib import admin
from .models import Logo,Category, Blog


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'status', 'is_featured', 'created_at')
    list_filter = ('status', 'is_featured', 'category', 'author')
    search_fields = ('title', 'id','category__category_name','status')
    list_editable = ('is_featured', 'status')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created_at', 'updated_at')

admin.site.register(Logo)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)