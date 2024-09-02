from django.db import models

class Cat001Estado(models.Model):
    nombre = models.CharField(max_length=255, blank=True, null=True)
    codigo = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return  self.nombre + ' ' + str(self.id)

    class Meta:
        managed = False
        db_table = 'cat_001_estado'
        ordering = ['id']

    verbose_name = 'ESTADO'
    verbose_name_plural = 'ESTADOS'

class Cat007TipoImagen(models.Model):
    estado_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    cod = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return  self.nombre + ' ' + str(self.id)
    
    class Meta:
        managed = False
        db_table = 'cat_007_tipo_imagen'
        ordering = ['id']

    verbose_name = 'TIPO IMAGEN'
    verbose_name_plural = 'TIPOS DE IMAGENES'