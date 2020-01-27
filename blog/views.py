from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/index.html', {'posts': posts})

def index(request):
    return render(request, 'blog/index.html')

def nosotros(request):
    return render(request, 'blog/nosotros.html')

def donaciones(request):
    return render(request, 'blog/donaciones.html')

def contacto(request):
    return render(request, 'blog/contacto.html')

def formulario(request):
    return render(request, 'blog/formulario.html')
# Create your views here.
