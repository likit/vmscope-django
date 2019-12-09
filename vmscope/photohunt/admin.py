from django.contrib import admin
from .models import *


class ImageAdmin(admin.ModelAdmin):
    list_display = ('parasite', 'image_dim', 'upload_by', 'upload_at', 'image_url')
    readonly_fields = ('image_tag', 'image_dim')


admin.site.register(Image, ImageAdmin)
admin.site.register(Parasite)
admin.site.register(ImageTagSet)
admin.site.register(ImageTag)
admin.site.register(Question)
admin.site.register(Session)
admin.site.register(Discipline)
admin.site.register(Program)
