from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/', include([
        re_path(r'^songs/', include('songs.urls', namespace='songs'))])),
]
