#!/usr/bin/python
# -*- coding: utf-8 -*-


fichero = open("/etc/passwd",'r')

while 1:
    lineas = fichero.readline()
    argumentos = lineas.split(":")
    usuario = argumentos[0]
    shell = argumentos[-1]
    print usuario, shell[:-1]
    if not lineas:
        break

fichero.close()
fichero = open("/etc/passwd",'r')
print "Hay", len(fichero.readlines()), "usuarios"
fichero.close()
