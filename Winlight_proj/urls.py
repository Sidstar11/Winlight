from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Winlight_app.views import studio_home, all_pipeline_projects, all_editorial_articles, all_recent_works, all_crew_members , studio_control_desk

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', studio_home, name='studio_home'),
    path('portfolio-archive/', all_recent_works, name='recent_archive'),
    path('pipeline-archive/', all_pipeline_projects, name='pipeline_archive'),
    path('editorial-archive/', all_editorial_articles, name='editorial_archive'),
    path('crew-archive/', all_crew_members, name='crew_archive'),
    path('studio-control/', studio_control_desk, name='control_desk'), # NEW ADMIN PANEL PATH
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)