# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Emp021InformacionPrincipal(models.Model):
    estado_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING)
    nit = models.IntegerField(blank=True, null=True)
    digito_verificacion = models.IntegerField(blank=True, null=True)
    razon_social = models.CharField(max_length=255, blank=True, null=True)
    mision = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    perfil = models.TextField(blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    correo = models.CharField(max_length=255, blank=True, null=True)
    celular = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_021_informacion_principal'


class Pro041Tipo(models.Model):
    estado_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING)
    nombre = models.CharField(unique=True, max_length=255)
    codigo = models.CharField(unique=True, max_length=3)

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
    nombre_archivo = models.CharField(max_length=255)
    tipo_007 = models.ForeignKey(Cat007TipoImagen, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pro_044_imagen'


class Pro045Marca(models.Model):
    estado_001 = models.ForeignKey(Cat001Estado, models.DO_NOTHING)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pro_045_marca'
