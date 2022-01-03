from django.urls import path
from . import views
from .views import Home, blog, search, CategoryView, blogdetail


urlpatterns = [
path('', Home.as_view(), name="index"),
path('blog', blog.as_view(), name="blog"),
path('search', search, name="search"),
path('category/<str:cats>/', CategoryView, name="category"),
path('<slug:slug>/send-comment', views.send_comment, name="send_comment"),
path('<slug:slug>/', blogdetail.as_view(), name="blog-detail"),
]
