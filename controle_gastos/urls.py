"""controle_gastos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from django.template.defaulttags import url
from django.urls import path, include
from contas.views import home, listagem, login, UsuarioCreate, PerfilUpdate, Perfiluser
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views

import controle_gastos.forms
import contas.views

urlpatterns = [
        path('admin/', admin.site.urls),
        path('waifu/', listagem, name="waifu"),
        path('home/', home, name="home"),
        path('accounts/', include('django.contrib.auth.urls')),
        path('login/', auth_views.LoginView.as_view(), name='login'),
        path('registrar/', UsuarioCreate.as_view(), name='registrar'),
        path('atualizar-dados/', PerfilUpdate.as_view(), name='atualizar-dados'),
        path('perfil/', Perfiluser.as_view(), name='perfil'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
