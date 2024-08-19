from django.db import models

class Cat001Estado(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_001_estado'

class Cat007TipoImagen(models.Model):
    estado_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    cod = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cat_007_tipo_imagen'