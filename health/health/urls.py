from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bloodpressures/', include('bloodpressures.urls')),
    path('glucoses/', include('glucoses.urls')),
]
