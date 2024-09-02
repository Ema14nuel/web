from django.db import models
from applications.common.models import Cat001Estado, Cat007TipoImagen

# Create your models here.
class Pro041Tipo(models.Model):
    estado_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING)
    nombre = models.CharField(unique=True, max_length=255)
    codigo = models.CharField(unique=True, max_length=3)

    def __str__(self):
        return  self.nombre + ' ' + str(self.id)
    
    class Meta:
        managed = False
        db_table = 'pro_041_tipo'


class Pro042Producto(models.Model):
    estado_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING)
    tipo_041 = models.ForeignKey(Pro041Tipo, models.DO_NOTHING)
    nombre = models.CharField(unique=True, max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    dimesion = models.CharField(max_length=255, blank=True, null=True)
    marca_045 = models.ForeignKey('Pro045Marca', models.DO_NOTHING)
    peso = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return  self.nombre
    
    class Meta:
        managed = False
        db_table = 'pro_042_producto'


class Pro043ProductoValor(models.Model):
    estado_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING)
    fecha_creacion = models.DateField()
    fecha_actualizacion = models.DateField(blank=True, null=True)
    producto_042 = models.ForeignKey(Pro042Producto, models.DO_NOTHING)
    valor = models.IntegerField()
    cantidad = models.IntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_043_producto_valor'


class Pro044Imagen(models.Model):
    estado_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING)
    producto_042 = models.ForeignKey(Pro042Producto, models.DO_NOTHING)
    imagen_083_id = models.IntegerField()
    nombre_archivo = models.ImageField(upload_to='producto', blank=True, null=True)  # Nuevo campo de imagen
    tipo_007 = models.ForeignKey(Cat007TipoImagen, models.DO_NOTHING)

    def __str__(self):
        return  self.nombre
    
    class Meta:
        managed = False
        db_table = 'pro_044_imagen'


class Pro045Marca(models.Model):
    estado_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='marca', blank=True, null=True)  # Nuevo campo de imagen

    class Meta:
        managed = False
        db_table = 'pro_045_marca'