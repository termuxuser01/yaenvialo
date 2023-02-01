from django.contrib import admin
from django.http import JsonResponse
from django.urls import path
from django.url import include


def test(request):
    return JsonResponse({"hola": "como estas?"})


urlpatterns = [
    path('', include('base.urls'))
    path("/test", test, name="test"),
    path("admin/", admin.site.urls),
]