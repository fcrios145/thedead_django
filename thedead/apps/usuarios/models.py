from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Usuario(models.Model):
    roles = (
        ('autor','Autor'),
        ('regular','Regular'),
    )
    usuario = models.OneToOneField(User)
    facebook = models.CharField(max_length=64, blank=True)
    twitter = models.CharField(max_length=64, blank=True)
    rol = models.CharField(max_length=64, choices=roles, default='regular')

    def __unicode__(self):
        return self.usuario.username