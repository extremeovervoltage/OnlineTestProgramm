from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^erstellen/', views.erstellen, name='erstellen'),
    url(r'^(?P<frage_id>[0-9]+)/$', views.frage_ansehen, name='frage_ansehen'),
]
