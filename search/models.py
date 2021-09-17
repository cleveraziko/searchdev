from django.db import models

from django.core.validators import MinLengthValidator

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=20)


    def __str__(self):
        return self.caption
    



class AuthorAddress(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)






class Author(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.OneToOneField(AuthorAddress, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} {self.last_name} "
    
    




class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts", null="True")
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(MinLengthValidator(10))
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True , related_name="posts")
    tag = models.ManyToManyField(Tag)



    def __str__(self):
        return self.title
    
    