

from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home2/', views.home2, name='home2'),
    path('product/', include('product.urls')),
    path('cart/', include('cart.urls')),
    path('news/', include('news.urls')),
    path('about/', include('about.urls')),
    path('shop/', views.shop, name='shop'),
    path('contact/', include('contact.urls')),
    path('promotions/', include('promotions.urls')),
    path('404/', views.page_not_found, name='page_not_found'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
