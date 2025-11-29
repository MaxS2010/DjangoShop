from django.db import models
from django.urls import reverse
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.PositiveIntegerField(null= True)
    
    def get_absolute_url(self):
        return reverse(viewname= "author_page", kwargs={'pk':self.pk})
    
