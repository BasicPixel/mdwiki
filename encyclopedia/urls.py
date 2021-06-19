from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('wiki/<str:entry>', views.entry, name='entry'),
    path('wiki/edit/<str:entry>', views.edit, name='edit'),
    path('wiki/save/<str:entry>', views.save_edit, name='save_edit'),
    path('new', views.new, name='new'),
    path('new/save', views.save_new, name='save_new'),
    path('random', views.get_random, name='random'),
    path('search', views.search, name='search')
]
