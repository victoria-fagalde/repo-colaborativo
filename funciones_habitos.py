#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:21:00 2026

@author: vickyfagalde
"""

def registrar_habitos():
    lista_actividades = []
    while True:
        actividad = input("Ingrese la actividad del dia: ")
        if actividad == "":
            break
        lista_actividades.append(actividad)
        
    return lista_actividades

'''
Recibe las actividades del usuario y las pone en una lista hasta que el usuario no ingrese más.

Parámetros
---------
lista_actividades: list
lista de actividades entradas por el usuario

actividad: str
la actividad del usuario

Returns
-------
list
la lista de actividades

'''
    
def analizar_habitos(lista):
    frecuencias = {}
    
    for actividad in lista:
        if actividad not in frecuencias:
            frecuencias[actividad] = 0
            
        frecuencias[actividad] +=1
        
    return frecuencias


'''
Cuenta la frecuencia de actividades en una lista y las pone en un diccionario

Parámetros
----------
lista: list
actividades a contar

frecuencias: diccionario
las variables son las actividades y sus valores la cantidad que fueron entradas

actividad: str
elemento de la lista

Returns
-------
diccionario
actividades con sus respectivas frecuencias
'''



