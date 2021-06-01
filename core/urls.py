from django.urls import path
from .views import HomeTemplateView,WorkPageView

urlpatterns = [
    path('work/', WorkPageView.as_view(), name='work'),
    path('', HomeTemplateView.as_view())
]
