# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

from .models import Author, Article, Category, Tag


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'authors_string', 'published']
    raw_id_fields = ['authors', 'tags']
    list_select_related = ['category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
