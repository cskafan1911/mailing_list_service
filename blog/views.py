from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView

from blog.forms import BlogForm
from blog.models import Blog


class BlogCreateView(LoginRequiredMixin, CreateView):
    """
    Класс для создания статей.
    """

    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """
    Класс для редактирования статей.
    """

    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')


class BlogDetailView(DetailView):
    """
    Класс для отображения информации отдельной статьи.
    """

    model = Blog

    def get_object(self, queryset=None):
        """
        Метод считает количество просмотров статьи.
        """
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()

        return self.object


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    """
    Класс для удаления статьи.
    """

    model = Blog
    success_url = reverse_lazy('blog:blog_list')


class BlogListView(ListView):
    """
    Класс для получения списка всех статей.
    """

    model = Blog

    def get_queryset(self, *args, **kwargs):
        """
        Метод для получения списка статей.
        """
        queryset = super().get_queryset(*args, **kwargs)

        return queryset
