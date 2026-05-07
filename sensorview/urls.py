"""
URLs principais do projeto SensorView
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('leituras/', include('leituras.urls')),
]
