from django.contrib import admin
from .views import *
from .models import *

admin.site.register(About)
admin.site.register(RecentWork)
admin.site.register(Skills)
admin.site.register(Experience)
