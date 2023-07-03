from django.urls import path
from .views import identify
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the bytespeed index.")


urlpatterns = [
    path('identify/', identify),
    path('index/', index, name='index')
]
