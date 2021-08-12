from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import UserRegisterForm, PostForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'catalog/starter.html')

def insertar(request):
    return render(request, 'catalog/Registro.html') 

def historial(request):
    return render(request, 'catalog/Historial.html') 

def feed(request):
	posts = Post.objects.all()

	context = { 'posts': posts}
	return render(request, 'social/feed.html', context) 

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('index')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'social/register.html', context)

def post(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Post enviado')
			return redirect('feed')
	else:
		form = PostForm()
	return render(request, 'social/post.html', {'form' : form })


def profile(request):
	return render(request, 'social/profile.html')	   
