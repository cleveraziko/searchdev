from django.urls  import path
from . import views

urlpatterns = [
    path("posts", views.IndexView.as_view()),
    path("posts/<slug:slug>", views.SingleListView.as_view(), name="detail")
]
