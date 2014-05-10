from django.db import models
from django.forms import ModelForm
from django.template.defaultfilters import slugify
from apps.usuarios.models import Usuario

# Create your models here.
from django.db.models.fields.related import ForeignKey


class Noticia(models.Model):
    slug = models.SlugField(('slug'), max_length=64, blank=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    titulo = models.TextField(max_length=64)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='imagen_noticias')
    autor = ForeignKey(Usuario)

    def save(self, *args, **kwargs):
        """
        Este metodo se activa cuando se guarda n nuevo registro en la tabla de noticias, genera una
        url bonita para posteriormente buscar el objeto
        """
        if not self.id:
            #Only set the slug when the object is created.
            self.slug = slugify(self.titulo) #Or whatever you want the slug to use
        super(Noticia, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.titulo

