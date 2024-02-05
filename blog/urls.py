from django.contrib.auth.views import LoginView
from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogUpdateView, BlogDetailView, BlogListView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/detail/', cache_page(60)(BlogDetailView.as_view()), name='blog_info'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),

]
