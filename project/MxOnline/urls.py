from django.conf.urls import url

from . import views
from django.conf.urls import url
from django.contrib import admin
app_name = '[MxOnline]'
urlpatterns = [
    url(r'^form/$', views.getform, name='form'),
    url(r'^admin/', admin.site.urls),
]
