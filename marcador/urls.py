#from django.conf.urls import url
#from marcador.views import bookmark_user
#from marcador.views import bookmark_list
from django.urls import re_path
from . import views

#app_name = 'marcador'
urlpatterns = [
    re_path(r'^user/(?P<username>[-\w]+)/$', views.bookmark_user, name='marcador_bookmark_user'),
    re_path(r'^$', views.bookmark_list, name='marcador_bookmark_list'),
]