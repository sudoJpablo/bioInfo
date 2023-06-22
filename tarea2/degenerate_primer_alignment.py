#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys 
import re

def main():
    if(len(sys.argv)!=3):
        print('Debe ejecutarse como ./degenerate_primer_alignment.py <Secuencia ADN> <Partidor Degenerado>')
        sys.exit()
    
    #symbolDic es el diccionario que contiene los codigos de cada partidor, para asi formar la expresion regular
    #En el caso del partidor ser S, entonces el codigo seria [GC] lo que quiere decir que es o G o C
    symbolDic = dict()
    symbolDic = {'G':'[G]',
            'A':'[A]',
            'T':'[T]',
            'C':'[C]',
            'R':'[GA]',
            'Y':'[TC]',
            'M':'[AC]',
            'K':'[GT]',
            'S':'[GC]',
            'W':'[AT]',
            'H':'[ACT]',
            'B':'[GTC]',
            'V':'[GCA]',
            'D':'[GAT]',
            'N':'[GATC]'}

    #Cadena recibe una secuencia de ADN y parDeg un partidor degenerado, ambos valores desde los argumentos 
    cadena = sys.argv[1]
    partDeg = sys.argv[2]

    #Forma la expresion regular para encontrar las similitudes en la cadena 
    deg= '('
    for i in partDeg:
        deg = deg + symbolDic[i]
    deg+= ')'  

    #coincidencias es un arreglo que guarda todas las coincidencias de la cadena con la expresion regular deg
    coincidencias = re.finditer(f'{deg}',cadena)
    print('pos seq')
    for match in coincidencias:
         print(f'{match.start()} {match.group()}')

if __name__ == "__main__":
        main()

