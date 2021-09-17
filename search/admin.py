from django.contrib import admin
from django.db import models
from .models import Post,Author,Tag, AuthorAddress 

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tag","date",)
    list_display = ("title", "date", "author")
    prepopulated_fields = {"slug": ("title",)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name","email")


class TagAdmin(admin.ModelAdmin):
    list_display = ("caption",)

class AuthorAddAmin(admin.ModelAdmin):
    list_display = ("city", "street",)


admin.site.register(Post, PostAdmin)
admin.site.register(AuthorAddress, AuthorAddAmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Author,AuthorAdmin)