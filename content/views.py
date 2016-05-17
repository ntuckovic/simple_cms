# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.views.generic import ListView, DetailView

from users.models import UserProfile

from .models import Article


class FrontpageView(ListView):
    template_name = 'content/frontpage.html'
    model = Article
    paginate_by = 50

    def get_queryset(self):
        normal_queryset = super(FrontpageView, self).get_queryset()
        user = self.request.user
        queryset = normal_queryset.filter(published=True)

        if self.request.user.is_authenticated():
            user_profile = UserProfile.objects.filter(user=user).first()

            if user_profile:
                personalized_queryset = normal_queryset.filter(
                    published=True,
                    category__in=user_profile.favorite_categories.all()
                )

                if personalized_queryset:
                    queryset = personalized_queryset

        return queryset


class ArticleView(DetailView):
    template_name = 'content/article.html'
    model = Article
