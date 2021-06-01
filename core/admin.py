from django.contrib import admin
from .views import *
from .models import *

admin.site.register(About)
admin.site.register(RecentWork)
admin.site.register(Experience)
admin.site.register(Journey)
admin.site.register(Duties)
admin.site.register(AllWork)

