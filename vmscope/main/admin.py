from django.contrib import admin
from .models import (Discipline, Program, Session)

# Register your models here.
class SessionAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'updated_at')


admin.site.register(Session, SessionAdmin)
admin.site.register(Program)
admin.site.register(Discipline)
