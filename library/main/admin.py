from django.contrib import admin

# my local models
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'author', 'isbn']
admin.site.register(Book, BookAdmin)