"""Supcon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from catalog import views
app_name = 'catalog'
urlpatterns = [
    #привязка адрреса /goods
    #path('',  views.catalog, name = "catalog"),
    path('',  views.good_detail.as_view(), name = "catalog"),
    path('<int:no>/',  views.good_detail.as_view(), name = "good"),
    path('cat/<int:cat>/',  views.good_detail.as_view(), name = "category"),
    path('scat1/<int:scat1>',  views.good_detail.as_view(), name = "scat1"),
    path('scat2/<int:scat2>',  views.good_detail.as_view(), name = "scat2"),
    path('scat3/<int:scat3>',  views.good_detail.as_view(), name = "scat3"),
    path('cat/<int:cat>/<int:no>/',  views.good_detail.as_view(), name = "category_good"),
    path('scat1/<int:scat1>/<int:no>/',  views.good_detail.as_view(), name = "scat1_good"),
    path('scat2/<int:scat2>/<int:no>/',  views.good_detail.as_view(), name = "scat2_good"),
    path('scat3/<int:scat3>/<int:no>/',  views.good_detail.as_view(), name = "scat3_good"),
    path('delete/<int:no>/',  views.good_delete.as_view(), name = "good_delete"),
    # привязка адреса конкретного товара    
   # path('<int:good_id>/',  views.id, name = "good_id"),
    # привязка адреса категории
   # path('cat/<int:cat_id>/',  views.cat, name = "category"),
    # привязка адреса /cat
   # path('cat/',  views.cat_home, name = "cat_home")
]
