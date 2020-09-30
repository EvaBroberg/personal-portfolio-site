from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import About, RecentWork, Skills, Experience

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    #override get context method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['works'] = RecentWork.objects.all()
        context['skills'] = Skills.objects.all()
        context['experiences'] = Experience.objects.all()
        
        return context