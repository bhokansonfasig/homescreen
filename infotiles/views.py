from django.shortcuts import render
from django.views.generic.base import TemplateView


class DesktopView(TemplateView):
    """View class for desktop-based tile layout"""
    template_name = "infotiles/desktop.html"

    def get_context_data(self, **kwargs):
        context = super(DesktopView,self).get_context_data(**kwargs)
        context['name'] = "Ben"
        return context
