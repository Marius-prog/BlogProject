from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# def hello(request):
#     return render(request, 'BlogApp/main.html')

class HomeView(ListView):
    model = Post
    template_name = 'BlogApp/main.html'