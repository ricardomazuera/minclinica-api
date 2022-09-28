from operator import mod
from unittest.util import _MAX_LENGTH
# from _tkinter import CASCADE
from django.db import models

class Persona(models.Model):
    id = models.BigIntegerField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=10)
    
class Paciente(models.Model):
    id = models.BigIntegerField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    birthday = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitud = models.FloatField()

class Familiar (models.Model):
    id = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    parentesco = models.CharField(max_length=15)
    email = models.EmailField()

class Medico(models.Model):
    id = models.BigIntegerField(primary_key=True)
    persona = models.ForeignKey(Persona,default=1, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=30)
    registro = models.BigIntegerField()

class EnfermeroAuxiliar (models.Model):
    id = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona, default=1, on_delete=models.CASCADE)
    password = models.CharField(max_length=30)

class JefeEnfermeria(models.Model):
    id = models.AutoField(primary_key=True)
    persona = models.ForeignKey(Persona,default=1, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)




