from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250)
    author = models.CharField(max_length=30)
    isbn = models.CharField(max_length=15)
    
    def __str__(self):
        return self.title[:12] + " | " + self.author
    
