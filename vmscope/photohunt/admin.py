from django.contrib import admin
from .models import *


admin.site.register(Image)
admin.site.register(Parasite)
admin.site.register(ImageTagSet)
admin.site.register(ImageTag)