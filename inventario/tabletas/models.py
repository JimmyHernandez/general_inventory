from django.db import models
#from django.contrib.auth.models import User  # Para relacionar con el usuario asignado

class NewTablet(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    fecha_compra = models.DateField()
    garantia = models.BooleanField(default=False)
    numero_serie = models.CharField(max_length=100, unique=True)
    numero_telefono = models.CharField(max_length=20, blank=True)
    numero_imei = models.CharField(max_length=15, unique=True)
    tipo_cargador = models.CharField(max_length=50)
    #asignado_a = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Relaciona con el usuario asignado
    tag_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.marca} - {self.modelo}"