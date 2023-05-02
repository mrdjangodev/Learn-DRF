from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date', 'updated_at']
    list_editable = ['title']
    
admin.site.register(Post, PostAdmin)