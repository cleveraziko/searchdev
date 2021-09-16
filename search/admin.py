from django.contrib import admin
from .models import Post,Author,Tag, AuthorAddress 

# Register your models here.

admin.site.register(Post)
admin.site.register(AuthorAddress)
admin.site.register(Tag)
admin.site.register(Author)