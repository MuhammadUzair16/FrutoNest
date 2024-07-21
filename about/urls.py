from django.urls import path
from .views import team_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', team_view, name='about'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
