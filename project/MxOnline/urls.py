from django.conf.urls import url

from . import views

app_name = '[MxOnline]'
urlpatterns = [
    url(r'^form/$', views.getform, name='form'),

]
