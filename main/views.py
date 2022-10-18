from multiprocessing import context
from urllib import request
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Blog
from .forms import BlogForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import UpdateView, DeleteView
import random

def index(request):
	"""Returns the 'index.html' page with an argument that is generic posts."""

	posts = Blog.objects.all().filter(share=1).order_by('-id')
	context = {
		'posts':posts
	}

	return render(request, 'main/index.html', context)

class BlogUpdateView(UpdateView):
	"""Updaetes post"""

	model =  Blog
	template_name = 'main/update_post.html'
	queryset = Blog.objects.all()
	form_class = BlogForm

class BlogDeleteView(DeleteView):
	"""Deletes post"""

	model =  Blog
	success_url = '/blogs'
	template_name = 'main/delete_post.html'
	queryset = Blog.objects.all()

def register_request(request):
	"""Receives data from the form. 
		If the data is valid, it is stored in the 
		database and redirected to the 'home' page, 
		otherwise an error message is returned.
	"""

	if request.user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, 'Registration successful.' )
			return redirect('home')
		messages.error(request, 'Unsuccessful registration. Invalid information.')
	form = NewUserForm()

	return render (request=request, template_name='main/register.html', context={'register_form':form})


def login_request(request):
	"""If the data is in the database, the system is authorized"""

	if request.user.is_authenticated:
		return redirect('home')
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f'You are now logged in as {username}.')
				return redirect('home')
			else:
				messages.error(request,'Invalid username or password.')
		else:
			messages.error(request,'Invalid username or password.')
	form = AuthenticationForm()

	return render(request=request, template_name='main/login.html', context={'login_form':form})


def logout_request(request):
	"""Logs out of the system"""

	logout(request)
	messages.info(request, 'You have successfully logged out.') 

	return redirect('home')


def add_post(request):
	"""Receives data from the form. 
		If the data is valid, it is stored in the 
		database and redirected to the 'blogs' page, 
		otherwise an error message is returned.
	"""

	if not request.user.is_authenticated:
		return redirect('home')
	error = ''
	if request.method == 'POST':
		form = BlogForm(request.POST, request.FILES)
		if form.is_valid():
			blog = form.save(commit=False)
			blog.owner = request.user
			blog.save()
			return redirect('blogs')
		else:
			error = 'Incorrect form'

	return render(request, 'main/add_post.html',{'form':BlogForm(),'error':error})


def blogs(request):
	"""Returns the 'blogs.html' page with an argument that is user posts."""

	if not request.user.is_authenticated:
		return redirect('home')
	posts = Blog.objects.all().filter(owner = request.user).order_by('-id')	

	return render(request, 'main/blogs.html', {'posts':posts})


def blogDetailView(request,pk):
	"""
	Arguments: post id
	Returns: Post detail page

	"""

	if not request.user.is_authenticated:
		return redirect('home')
	blog = Blog.objects.get(id=pk)

	return render(request,'main/blog_detail_view.html', {'post':blog})


def postDetailView(request,pk):
	"""
	Arguments: post id
	Returns: Shared post detail page

	"""
	blog = Blog.objects.get(id=pk)
	posts = list(Blog.objects.filter(share=1).exclude(id=pk))
	posts= random.sample(posts, 4)

	return render(request,'main/post_detail_view.html', {'post':blog,'posts':posts})


def share_post(request,pk):	
	"""
	Arguments: post id
	Returns: Shared post

	"""
	if not request.user.is_authenticated:
		return redirect('home')
	post = Blog.objects.get(id=pk)
	post.share = 1
	post.save()

	return redirect('post_detail',pk=pk)


def search(request):
	"""Returns search result page"""
	
	if request.method == 'POST':
		search = request.POST['search']

	posts_title = Blog.objects.filter(title__contains=search,share=1).order_by('-id')
	posts_description = Blog.objects.filter(description__contains=search,share=1).order_by('-id')
	posts_owner = Blog.objects.filter(owner__contains=search,share=1).order_by('-id')
	posts = set(list(posts_title) + list(posts_description) + list(posts_owner))
	posts = list(posts)

	return render(request,'main/search.html',{'posts':posts})
	

