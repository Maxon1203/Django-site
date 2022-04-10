from ast import If
from cgitb import text
from dataclasses import field
from distutils import command
from distutils.errors import CompileError
import profile
from pydoc import pager
from pyexpat import model
from turtle import pos
from django import forms
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.template import context
from tomlkit import comment
from .models import *
from .forms import CommentForm, PostCreateForm, Tag_Form, UserUpdateForm
from django.views.generic import View, ListView
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from django.core.paginator import Paginator
from django.db.models import Q


def index_tag(request):
    tags = Tag.objects.all()

    paginator = Paginator(tags, 4)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    return render(request, template_name='news/index_tag.html', context={'page_tags': page, 'is_paginated': is_paginated, 'prev_url': prev_url, 'next_url': next_url})


def index(request):
    search_request = request.GET.get('search', '')
    if search_request:
        post_list = Post.objects.filter(
            Q(title__icontains=search_request) | Q(text__icontains=search_request))
    else:
        post_list = Post.objects.all()

    paginator = Paginator(post_list, 5)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    return render(request, template_name='news/index.html', context={'posts_var': page, 'is_paginated': is_paginated, 'prev_url': prev_url, 'next_url': next_url})


def index_filter(request, tag_id):
    tags = Tag.objects.all()
    postss = Post.objects.filter(tag_duraction=tag_id)


# def post_detail(request, id_post):
#     try:
#         # select * from Post where id = 'id_post'
#         post = Post.objects.get(id=id_post)
#         context = {'post': post, 'form': CommentForm}
#     except Post.DoesNotExist:
#         Http404('Статья не найдена')
#     return render(request, 'news\\post_detail.html', context)
def post_detail(request, id_post):
    try:
        # select * from Post where id = 'id_post'
        post = Post.objects.get(id=id_post)

        comments = post.comment_set.all()
    except Post.DoesNotExist:
        Http404('Статья не найдена')

    paginator = Paginator(comments, 3)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    return render(request, 'news\\post_detail.html', context={'post': post, 'comments': page, 'form': CommentForm, 'is_paginated': is_paginated, 'prev_url': prev_url, 'next_url': next_url})


# @permission_required('comment.can_add_комментариии')
@ login_required
def add_comment(request, id_post):
    form = CommentForm(request.POST)
    post = get_object_or_404(Post, id=id_post)

    if form.is_valid():
        comment = Comment()
        comment.text = form.cleaned_data['comment']
        comment.author = User(id=request.user.id)
        comment.fk_post = post
        comment.save()
    return redirect(post.get_absolute_url())


class PostCreate(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = ('post.can_add_post',)
    raise_exception = True

    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        return render(request, 'news\\post_create_form.html',
                      {'form': form})

    def post(self, request, *args, **kwargs):
        filled_form = PostCreateForm(request.POST)

        if filled_form.is_valid():
            post = Post()
            post.title = filled_form.cleaned_data['title']
            post.text = filled_form.cleaned_data['text']
            post.author = User(id=request.user.id)
            post.save()

            tag_array = filled_form.cleaned_data['tag_state']

            for tag_item in tag_array:
                post.tag_state.add(Tag.objects.get(text=tag_item))

            return redirect(post.get_absolute_url())
        return render(request, 'news\\post_create_form.html', {'form': filled_form})


class PostUpdate(View):

    def get(self, request, id_post):
        post = Post.objects.get(pk=id_post)
        form = PostCreateForm(instance=post)
        return render(request, 'news\\post_update_form.html', context={'form': form, 'obj': post})

    def post(self, request, id_post):
        post = Post.objects.get(pk=id_post)
        form = PostCreateForm(request.POST, instance=post)

        if form.is_valid():
            new_obj = form.save()
            return redirect(new_obj)
        return render(request, 'news\\post_update_form.html', context={'forn': form, 'obj': post})


class PostDelete(View):

    def get(self, request, id_post):
        post = Post.objects.get(pk=id_post)
        return render(request, 'news\\post_delete_form.html', context={'obj': post})

    def post(self, request, id_post):
        post = Post.objects.get(pk=id_post)
        post.delete()
        return redirect(reverse('index_url'))


class TagCreateView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = ('post.can_add_post',)
    raise_exception = True

    def get(self, request, *args, **kwargs):
        form = Tag_Form()
        return render(request, 'news\\tag_create_form.html', {'foгm': form})

    def post(self, request, *args, **kwargs):
        fielld_form = Tag_Form(request.POST)
        if fielld_form.is_valid():
            tag = Tag()
            tag.text = fielld_form.cleaned_data['text']
            tag.save()

        return render(request, 'news\\tag_create_form.html', {'form': fielld_form})


class TagUpdate(View):
    def get(self, request, tag_id):
        tag = Tag.objects.get(pk=tag_id)
        form = Tag_Form(instance=tag)
        return render(request, 'news\\tag_update_form.html', context={'form': form, 'obj': tag})

    def post(self, request, tag_id):
        tag = Tag.objects.get(pk=tag_id)
        form = Tag_Form(request.POST, instance=tag)
        if form.is_valid():
            new_obj = form.save()
            return redirect(reverse('index_url'))
        return render(request, 'news\\tag_update_form.html', context={'form': form, 'obj': tag})

    # Класс удаления тега с обработкой GET и POST запросов


class TagDelete(View):
    def get(self, request, tag_id):
        tag = Tag.objects.get(pk=tag_id)
        return render(request, 'news/tag_delete_form.html', context={'obj': tag})

    def post(self, request, tag_id):
        post = Tag.objects.get(pk=tag_id)
        post.delete()
        return redirect(reverse('index_url'))


class UserUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        data_obj = User.objects.get(username=request.user.username)
        bound_form = UserUpdateForm(instance=data_obj)
        return render(request, 'news/user_account.html', context={'form': bound_form, 'obj': data_obj})

    def post(self, request):
        data_obj = User.objects.get(username=request.user.username)
        bound_form = UserUpdateForm(request.POST, instance=data_obj)
        if bound_form.is_valid():
            bound_form.save()
            return redirect("profile_detail_url")
        return render(request, 'news/user_account.html', context={'form': bound_form, 'obj': data_obj})


class UserPostsListView(ListView):
    model = Post
    template_name = 'news/posts_list.html'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user.id).order_by('pub_date')
