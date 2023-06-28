"""
URL configuration for cafe project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, re_path
from django.contrib.auth.views import LoginView, logout_then_login
from apps.compra.views import index


urlpatterns = [
    #path('admin/', admin.site.urls),
    re_path(r'^$', index, name='index'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^compra/', include('apps.compra.urls')),
    re_path(r'^usuario/', include('apps.usuario.urls')),
    re_path(r'^accounts/login/', LoginView.as_view(template_name="usuario/index.html"),name="login"),
    re_path(r'^logout/', logout_then_login, name='logout'),
    
]


