from django.contrib import admin
from django.http import JsonResponse
from django.urls import path


def home(request):
    return JsonResponse({"hola": "como estas?"})


urlpatterns = [
    path("/test", test, name="test"),
    path("admin/", admin.site.urls),
]
