"""maximsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path, re_path, reverse_lazy
from django.contrib.auth.views import login, logout
from marcador import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    re_path(r'^', include("marcador.urls")),
    re_path(r'^create/$', views.bookmark_create,
        name='marcador_bookmark_create'),
    re_path(r'^edit/(?P<pk>\d+)/$', views.bookmark_edit,
        name='marcador_bookmark_edit'),
    re_path(r'^login/$', login, {'template_name': 'login.html'},
        name='mysite_login'),
    re_path(r'^logout/$', logout,
        {'next_page': reverse_lazy('marcador_bookmark_list')}, name='mysite_logout'),
]
