from django.db import models
from django.urls import reverse

from author_app.models import Author
# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=50)
    # author = models.CharField(max_length=50)
    date = models.PositiveIntegerField(null=True)
    author = models.ForeignKey(to= Author, on_delete= models.CASCADE, null = True)
    
    def get_absolute_url(self):
        return reverse(viewname="book_url", kwargs={"pk": self.pk})
    