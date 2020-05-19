from django.db import models


from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
import uuid

class Temperature(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.CharField(verbose_name='Fecha', max_length=20,default="x")
    origen = models.CharField(verbose_name='Origen', max_length=20,default="x")
    valor = models.IntegerField(verbose_name='Valor',default=0, validators = [MinValueValidator(0.0)])
    codigos = models.CharField(max_length=20, verbose_name='Codigos',default="hola")
    observacion = models.CharField(verbose_name='Observacion', max_length=30,default="x")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)