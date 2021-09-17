from django.db.models import query
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DeleteView
from .models import Post
# Create your views here.

class IndexView(ListView):
    template_name = "index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"


    def get_queryset(self):
        queryset = super().get_queryset()
        date = queryset[:3]
        return date    


class SingleListView(DeleteView):
    template_name = "news.html"
    model = Post
    # queryset = Post.objects.all()
    # context_object_name = "post"