from django.contrib import admin
from django.urls import path, include
from digitalmenu import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('digitalmenu.urls')),
]
