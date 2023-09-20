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
from django.urls import include, re_path, path
from django.contrib.auth.views import LoginView, logout_then_login
from apps.venta.views import index
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views


urlpatterns = [
    #path('admin/', admin.site.urls),
    re_path(r'^$', index, name='index'),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^venta/', include('apps.venta.urls')),
    re_path(r'^usuario/', include('apps.usuario.urls')),
    re_path(r'empleados/', include('apps.empleados.urls')),
    re_path(r'cliente/', include('apps.cliente.urls')),
    re_path(r'Productos/', include('apps.Productos.urls')),
    re_path(r'inv/', include(('apps.inv.urls', 'inv'), namespace='inv')),
    re_path(r'cmp/', include(('apps.cmp.urls', 'cmp'), namespace='cmp')),
    re_path(r'^accounts/login/', LoginView.as_view(template_name="usuario/index.html"),name="login"),
    re_path(r'^logout/', logout_then_login, name='logout'),
    re_path(r'reset_password/', auth_views.PasswordResetView.as_view(template_name="auten/password-reset.html"), name='password_reset'),
    re_path(r'reset_password_send/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    re_path(r'reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name="auten/password-confirm.html"), name='password_reset_confirm'),
    re_path(r'reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


