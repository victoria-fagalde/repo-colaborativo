#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:04:48 2026

@author: vickyfagalde
"""
import funciones_habitos

lista = funciones_habitos.registrar_habitos()

resultado = funciones_habitos.analizar_habitos(lista)

print(f"Resumen de actividades: la lista de hábitos registrados es: {lista}. La cantidad de veces que una actividad fue insertada se verá abajo")
print(resultado)
