from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from .models import Post, Comment
from .forms import PostForm, CommentForm
from .filters import PostFilter


# Create your views here.


class PostsList(ListView):
    model = Post
    ordering = 'date'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(FormMixin, DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_success_url(self, **kwargs):
        return reverse_lazy('post_detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class CommentDetail(DetailView):
    model = Comment
    template_name = 'post.html'
    context_object_name = 'comment'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
