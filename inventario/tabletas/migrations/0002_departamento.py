# Generated by Django 5.1.3 on 2024-11-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabletas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('07', '07'), ('30', '30'), ('REC', 'REC'), ('DTOP', 'DTOP'), ('EDUCACION', 'EDUCACION'), ('ORNATO', 'ORNATO'), ('IT', 'IT'), ('ORQUIDEA', 'ORQUIDEA'), ('OFICINA', 'OFICINA')], max_length=100, unique=True)),
            ],
        ),
    ]