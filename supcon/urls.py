"""supcon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
#оключение кэширования статик файлов
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache
from supcon import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/',  include('catalog.urls')),
]
#оключение кэширования статик файлов
if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
