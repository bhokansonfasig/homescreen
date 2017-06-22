from django.shortcuts import render
from django.views.generic.base import TemplateView


class DesktopView(TemplateView):
    """View class for desktop-based tile layout"""
    template_name = "infotiles/desktop.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Ben"
        return context


class BaseTileView(TemplateView):
    """View base calss for single tile"""
    template_name = "infotiles/tilebase.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
