#!/usr/bin/env python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
from django.db import models
from configuracion.models import Programa

# Create your models here.
class CodigoAcceso(models.Model):
    Codigo = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.Codigo)

class TipoPersona(models.Model):
    Tipo_persona = models.CharField(max_length=50, null=True)
    def __str__(self):
        return str(self.Tipo_persona)

class Personas(models.Model):

    ESTADO_TARJETA = (
        ('ACTIVA', 'ACTIVA'),
        ('INACTIVA', 'INACTIVA'),
    )
    Nro_Tarjeta = models.CharField(max_length=50, null=False, unique=True)
    Nro_Documento = models.CharField(max_length=80,null=False)
    Nombres = models.CharField(max_length=80)
    Apellidos = models.CharField(max_length=80)
    Estado_Tarjeta = models.CharField(max_length=30, choices=ESTADO_TARJETA)
    Tipo_Persona = models.ForeignKey(TipoPersona, null=True)
    Dependencia = models.ForeignKey(Programa, null=True)
    Codigo_Acceso = models.ForeignKey(CodigoAcceso, null=True)

    class Meta:
        verbose_name_plural = "Personas"

    def __str__(self):
        return str(self.Nro_Tarjeta)
