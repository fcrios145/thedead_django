from django.conf.urls import patterns, include, url
from .views import About

urlpatterns = patterns('',
    # Examples:
    url(r'^about$', About.as_view(), name='about'),


)

