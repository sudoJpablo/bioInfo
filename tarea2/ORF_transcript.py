#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re

def funcion(cadena, ini, fin):
    i = re.search(f'{ini}', cadena)
    f = re.search(f'{fin}', cadena)#Este no me sirve, tengo que despues de encontrar el primero
    #buscar de tres en tres las coicidencias de los stop
    print(f'{i.group()},{i.start()} {f.group()},{f.start()}')
    return cadena[i.start():f.end()]

def main():
    if len(sys.argv) != 2:
        print('Debe ejecutarse como ./ORF_transcript.py <Secuencia ADN>')
        sys.exit()

    secuencia = sys.argv[1]
    start = 'AUG|ATG'
    stop = 'UAA|UAG|UGA|TAA|TAG|TGA'

    # marcos de lectura
    for i in range(2):
        print(f'\nMarco de lectura {i}:')
        orf = funcion(secuencia[i:], start, stop)
        print(orf)

if __name__ == "__main__":
    main()

