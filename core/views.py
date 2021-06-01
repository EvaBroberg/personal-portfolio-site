from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import About, RecentWork, Experience, Journey, AllWork

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    #override get context method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['about']       = About.objects.first()
        context['works']       = RecentWork.objects.all()
        context['experiences'] = Experience.objects.all()
        context['journey']     = Journey.objects.all()
        
        return context

class WorkPageView(TemplateView): 
    template_name = 'work.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['allWork'] = AllWork.objects.all()
        
        return context
