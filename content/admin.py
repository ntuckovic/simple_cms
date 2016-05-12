# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin

from .models import Article, Category, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'author', 'published']
    raw_id_fields = ['author', 'tags']
    list_select_related = ['category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
