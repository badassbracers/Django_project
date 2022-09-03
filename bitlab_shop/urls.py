from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render

from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return render(request, 'index.html')


urlpatterns = [
    path('shop/', include('shop.urls')),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

