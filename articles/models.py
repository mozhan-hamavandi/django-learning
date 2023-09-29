from django.db import models

# Create your models here.

class Article(models.Model):

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    intro = models.TextField(max_length=300)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.title
    
#null=False, unique=True