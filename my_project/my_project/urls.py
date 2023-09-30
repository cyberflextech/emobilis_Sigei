from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('sigei.urls')),
    path('', admin.site.urls),
]
