from django.urls import include, path
from django.contrib import admin
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def index(request):
    return HttpResponse("Hello, world. You're at the bytespeed index.")




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('contact.urls')),
    path('index/', index, name='index')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
