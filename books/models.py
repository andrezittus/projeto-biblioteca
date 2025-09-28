from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    co_authors = models.CharField(max_length=255, blank=True, null=True)
    publisher = models.CharField(max_length=255) 
    publication_year = models.PositiveSmallIntegerField(blank=True, null=True) 
    edition = models.CharField(max_length=50) 
    create_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.title} by {self.author}'

