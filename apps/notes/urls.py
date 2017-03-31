from django.conf.urls import url
from . import views

app_name = "notes"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create$', views.create, name="create"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="delete"),
    url(r'^partial$', views.partial, name="partial"),
]
