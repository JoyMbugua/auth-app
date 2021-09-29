from django.urls import path
from django.conf.urls import url
from .views import home_view

urlpatterns = [ 
    path('', home_view, name='homeview'),
    url(r'^.*/$', home_view)
]