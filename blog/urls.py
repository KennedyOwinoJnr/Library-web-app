from django.urls import path
from .views import (PostlistView, PostDetailView,
                     PostCreateView, PostUpdateView,
                       PostDeleteView, UserPostlistView)
from . import views

urlpatterns = [
    path("", PostlistView.as_view(), name = 'blog-home'),
    path("user/<str:username>", UserPostlistView.as_view(), name = 'user-post'),
    path("post/<int:pk>/", PostDetailView.as_view(), name = 'post-detail'),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name = 'post-update'),
    path("post/new/", PostCreateView.as_view(), name = 'post-create'),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name = 'post-delete'),
    path("about/", views.about, name = 'blog-about'),

]

#add about page