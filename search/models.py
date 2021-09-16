from django.db import models

from django.core.validators import MinLengthValidator
from django.db.models.deletion import CASCADE

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)




class AuthorAddress(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)






class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.OneToOneField(AuthorAddress, on_delete=CASCADE)
    




class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField()
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(MinLengthValidator(10))
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True , related_name="posts")
    tag = models.ManyToManyField(Tag)
    