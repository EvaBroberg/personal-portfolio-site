from django.shortcuts import render
from django.views.generic import TemplateView

class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    #override get context method
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['about'] = About.objects.first()
    #     context['services'] = Service.objects.all()
    #     context['works'] = RecentWork.objects.all()
    #     return context

