from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'arqueria/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'arqueria/post_detail.html', {'post': post})

# Vista para listar todos los posts
class PostListView(ListView):
    model = Post
    template_name = 'arqueria/post_list.html'

# Vista para ver los detalles de un post específico
class PostDetailView(DetailView):
    model = Post
    template_name = 'arqueria/post_detail.html'

# Vista para crear un nuevo post
class PostCreateView(CreateView):
    model = Post
    fields = ['titulo', 'autor', 'contenido', 'imagen_destacada']
    template_name = 'arqueria/post_form.html'

# Vista para actualizar un post existente
class PostUpdateView(UpdateView):
    model = Post
    fields = ['titulo', 'autor', 'contenido', 'imagen_destacada']
    template_name = 'arqueria/post_form.html'

# Vista para eliminar un post
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'arqueria/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
