from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from placesremember import settings

from placesremember_app.views import pageNotFound

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("placesremember_app.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
