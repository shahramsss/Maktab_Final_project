from django.db.models.query_utils import Q
from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render, redirect
from django.http import HttpResponse, response
from .models import Category, Post, Comment, Tag
from django.views.generic import ListView, DetailView
from .froms import *
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required




def posts(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': list(posts)})

@login_required(login_url='login_view')
def post_detail_by_id(request, post_id):
    post = Post.objects.get(id=post_id)
    form = FormComment()
    comments = Comment.objects.filter(post=post_id)
    post_category = list(Post.objects.filter(id=post_id).prefetch_related('category'))
    if request.method == "POST":
        form = FormComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            
            comment.save()

    return render(request, 'detail.html', {'post': post, 'post_category': post_category, 'commnets': comments , 'form':form})

@login_required(login_url='login_view')
def post_detail_by_slug(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    comment = Comment.objects.filter(post__title=post_slug)
    post_category = list(Post.objects.filter(
        slug=post_slug).prefetch_related('category'))
    return render(request, 'detail.html', {'post': post, 'post_category': post_category, 'commnets': comment})


def categorys(request):
    categorys = Category.objects.all()
    return render(request, 'new_categorys.html', {'categorys': categorys})

@login_required(login_url='login_view')
def category_details(request, category_title):
    posts = Post.objects.filter(category__title=category_title)

    return render(request, 'category_details.html', {'posts': posts})


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "post_list_view.html"


class GetPost(DetailView):
    model = Post
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "post_slug"
    template_name = "post_detail_view.html"

@login_required(login_url='login_view')
def add_user(request):
    form = FormUser()
    if request.method == 'POST':
        form = FormUser(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'add_user.html', {'form': form})


def register(request):
    form = NewUserForm(None or request.POST)
    if request.method == 'POST':
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            login(request, user)
            return redirect(reverse("posts"))

    return render(request, 'register_form.html', {'form': form})


class Tags(ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "tag_list_view.html"

@login_required(login_url='login_view')
def filter_posts(request, category):
    posts = Post.objects.filter(category__title=category)
    return render(request, 'index.html', {'posts': list(posts)})

@login_required(login_url='login_view')
def add_category(request):
    form = FormCategory()
    if request.method == "POST":
        form = FormCategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('categorys'))

    return render(request, 'add_category.html', {'form': form})

@login_required(login_url='login_view')
def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    form = FormCategory(instance=category)
    if request.method == "POST":
        form = FormCategory(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect(reverse('categorys'))
    return render(request, 'edit_category.html',  {'form': form})

@login_required(login_url='login_view')
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    form = FormDeleteCategory(instance=category)
    if request.method == "POST":
        category.delete()
        return redirect(reverse('categorys'))

    return render(request, 'delete_category.html', {'form': form, 'category': category})

@login_required(login_url='login_view')
def new_post(request):

    form = FormPots()
    if request.method == "POST":
        form = FormPots(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.writer = request.user
            post.save()
            return redirect(reverse('posts'))

    return render(request, 'new_post.html', {'form': form})


def tag_filter_post(request, tag):
    posts = Post.objects.filter(tag__title=tag)
    return render(request, 'index.html', {'posts': list(posts)})

@login_required(login_url='login_view')
def add_tag(request):
    form = FormTag()
    if request.method == "POST":
        form = FormTag(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('tags'))
    return render(request, 'add_tag.html', {'form': form})

@login_required(login_url='login_view')
def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    form = FormTag(instance=tag)
    if request.method == "POST":
        tag.delete()
        return redirect(reverse('tags'))

    return render(request, 'delete_tag.html', {'form': form, 'tag': tag})

@login_required(login_url='login_view')
def edit_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    form = FormTag(instance=tag)
    if request.method == "POST":
        form = FormTag(request.POST, instance=tag)
        if form.is_valid():
            print("isvalid ")
            form.save()
            return redirect(reverse('tags'))
    return render(request, 'edit_tag.html',  {'form': form, 'tag': tag})


def search(request):
    search_term = ''

    if 'search' in request.GET:
        search_term = request.GET['search']        
        posts = Post.objects.filter(
        Q(title__icontains=search_term) | Q(description__icontains=search_term))
        return render(request, 'index.html', {'posts': list(posts)})

    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': list(posts)})


def register2(request):
    form = UserRegistrationForm()
    
    if request.method == 'POST':
        form = UserRegistrationForm(None or request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password1'] ,form.cleaned_data['password2'])
            login(request, user)
            return redirect(reverse("posts"))

    return render(request,'register_form_02.html',{'form': form})


def login_view(request):
    form = UsersLoginForm()
    if request.method == 'POST':
        form = UsersLoginForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect(reverse("posts"))
    return render(request, "login_form.html", {"form" : form,"title" : "Login",})