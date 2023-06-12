from django.db import models

# Create your models here.



# Create your views here.
class Book(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    isbn = models.CharField(max_length=13)
    
    def __str__(self) -> str:
        return self.title[:15]