from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from .models import Noticia

# Create your views here.
from south.creator.freezer import model_dependencies


class Index(ListView):
    template_name = 'noticias/index.html'
    context_object_name = 'noticias'
    def get_queryset(self):
        noticias = Noticia.objects.all()[:3]
        return noticias


class Listar(ListView):
    model = Noticia
    template_name = 'noticias/noticias_lista.html'
    context_object_name = 'noticias'

# views.py
class NoticiaDetalle(DetailView):
    model = Noticia
    template_name = 'noticias/detalle.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'noticia'

