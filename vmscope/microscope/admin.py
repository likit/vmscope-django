from django.contrib import admin
from .models import *


class ParasiteImageAdmin(admin.ModelAdmin):
    list_display = ('parasite', 'image_dim', 'upload_by', 'upload_at', 'image_url')
    readonly_fields = ('image_tag', 'image_dim')

class ArtifactImageAdmin(admin.ModelAdmin):
    list_display = ('artifact', 'image_dim', 'upload_by', 'upload_at', 'image_url')
    readonly_fields = ('image_tag', 'image_dim')

# Register your models here.
admin.site.register(ParasiteImage, ParasiteImageAdmin)
admin.site.register(Parasite)
admin.site.register(ParasiteStage)
admin.site.register(ArtifactImage, ArtifactImageAdmin)
admin.site.register(ArtifactType)
admin.site.register(Artifact)
admin.site.register(MicroscopeSection)
admin.site.register(ParasiteComponent)
admin.site.register(ArtifactComponent)
admin.site.register(ParasitePage)
admin.site.register(MicroscopePlayRecord)
