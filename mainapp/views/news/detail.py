__all__ = ['NewsDetailView']

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.views.generic import DetailView

from mainapp.models import News


class NewsDetailView(DetailView):
    model = News
    # template_name = "mainapp/news/news_detail.html"