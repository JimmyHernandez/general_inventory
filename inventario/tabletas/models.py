from django.db import models
#from django.contrib.auth.models import User  # Para relacionar con el usuario asignado

class Departamento(models.Model):
    nombre = models.CharField(max_length=100, unique=True, choices=[
        ('07' , '07'),
        ('30' , '30'),
        ('REC' , 'REC'),
        ('DTOP' , 'DTOP'),
        ('EDUCACION' , 'EDUCACION'),
        ('ORNATO' , 'ORNATO'),
        ('IT' , 'IT'),
        ('ORQUIDEA' , 'ORQUIDEA'),
        ('OFICINA' , 'OFICINA')
       ])  # Asegurar que cada nombre sea único
    

class Tabletas(models.Model):
    usuario = models.CharField(max_length=200)
    email_address = models.EmailField()
    classification = models.CharField(max_length=50, choices=[
        ('GENERAL FOREMAN' , 'GENERAL FOREMAN'),
        ('CREW LEADER' , 'CREW LEADER')
        # Add more choices as needed
    ])
    area = models.CharField(max_length=50, choices=[
            ('ARECIBO 1' , 'ARECIBO 1'),
            ('ARECIBO 2' , 'ARECIBO 2'),
            ('ARECIBO 3' , 'ARECIBO 3'),
            ('ARECIBO 4' , 'ARECIBO 4'),
            ('SAN JUAN' , 'SAN JUAN'),
            ('HERBICIDA' , 'HERBICIDA'),
            ('SUB ESTACIONES' , 'SUB ESTACIONES'),
            ('VINES' , 'VINES'),
            ('MAYAGUEZ 1' , 'MAYAGUEZ 1'),
            ('MAYAGUEZ 2' , 'MAYAGUEZ 2')
   
        # Add more choices as needed
    ])
    telefono = models.CharField(max_length=20)
    dispositivo = models.CharField(max_length=10, choices=[
        ('Ipad', 'Ipad'),
        ('Tablet', 'Tablet')
    ])
    imei = models.CharField(max_length=20, unique=True)
    sim_card = models.CharField(max_length=20, unique=True)
    version = models.CharField(max_length=50)
    puerto_de_carga = models.CharField(max_length=50, choices=[
        ('USB-C' , 'USB-C'),
        ('Lightning' , 'Lightning')
        # Add more choices as needed
    ])
    tag_id = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50, choices=[
        ('07' , '07'),
        ('30' , '30'),
        ('REC' , 'REC'),
        ('DTOP' , 'DTOP'),
        ('EDUCACION' , 'EDUCACION'),
        ('ORNATO' , 'ORNATO'),
        ('IT' , 'IT'),
        ('ORQUIDEA' , 'ORQUIDEA'),
        ('OFICINA' , 'OFICINA')
        # Add more choices as needed
    ])
    last_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
            return f"{self.area} - {self.tag_id}"
    
    
    