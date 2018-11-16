from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls

from microscope import urls as microscope_urls
from main import urls as main_urls
from api import urls as api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^cmsadmin/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^pages/', include(wagtail_urls)),
    path('microscope/', include(microscope_urls)),
    path('api/', include(api_urls)),
    path('', include(main_urls), name='main'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
