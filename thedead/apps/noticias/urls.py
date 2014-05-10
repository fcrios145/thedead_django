from django.conf.urls import patterns, include, url

from .views import Index, Listar, NoticiaDetalle

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Index.as_view(), name='home'),
    url(r'^noticias$', Listar.as_view(), name='noticias'),
    url(r'^noticias/(?P<slug>[-\w]+)/$', NoticiaDetalle.as_view(), name='noticiaDetalle'),
    # url(r'^genero$', genero.as_view(), name='genero'),
    # url(r'^blog/', include('blog.urls')),


)
