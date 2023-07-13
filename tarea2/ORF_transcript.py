#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
"""
#Tarea 2 
#Grupo 
- Andrade   , Jorge       - jorge.andrade01@alumnos.uach.cl 
- Fuentes   , Sebastian   - sebastian.fuentes02@alumnos.uach.cl 
- Pezo      , Juan Pablo  - juan.pezo@alumnos.uach.cl 
- Pinilla   , Claudio     - claudio.pinilla@alumnos.uach.cl
"""

def funcion(cadena, fin):
    condicion= False #Cuando sea false no se agragaran elementos a orf
    cont=3 #Para ir de 3 en 3 en la cadena
    orf = '' #Este se encarga de reunir los codones que forman el ORF
    orfs = [] #Aqui se guardan los ORFs obtenidos en el marco de lectura
    while(cont <= len(cadena)):
        codon = cadena[cont-3:cont]
        if(codon== 'ATG' or codon== 'AUG'):
            condicion = True
        if(condicion):
            orf+= codon
        if(fin.find(codon)!=-1 and condicion):
            condicion=False
            orfs.append(orf)
            orf=''
        cont+=3
    return orfs

def obtener_hebra_negativa(secuencia):
    complemento = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    hebra_negativa = ''.join(complemento[base] for base in reversed(secuencia))
    return hebra_negativa

def imprime(orf,cadena,signo,dict):
    for i in orf:
        print(f'{i} {cadena.find(i)} {len(i)} {signo} {transcripcion(i)}')

def transcripcion(orf):
    #Diccionario que guarda las transcripciones a proteina de cada codon
    diccionario={
        'GG[UCAGT]':'G',
        'GA[GA]':'E',
        'GA[CUT]':'D',
        'GC[UCAGT]':'A',
        'G[UT][UCAGT]':'V',
        'AG[GA]':'R',
        'AG[CUT]':'S',
        'AA[GA]':'K',
        'AA[CUT]':'N',
        'AC[UCAGT]':'T',
        'A[UT]G':'M',
        'A[UT][ACUT]':'I',
        'CG[UCAGT]':'R',
        'CA[GA]':'Q',
        'CA[CUT]':'H',
        'CC[UCAGT]':'P',
        'C[UT][UCAGT]':'L', 
        '[UT][UT][UCT]':'F',
        '[UT][UT][AG]':'L',
        '[UT]C[UCAGT]':'S',
        '[UT]A[UCT]':'Y',
        '[UT]A[AG]':'',
        '[UT]G[UCT]':'C',
        '[UT]GA':'',
        '[UT]GG':'W',        
    }
    
    proteina = ''
    for i in range(0, len(orf), 3):
        codon = orf[i:i+3]
        for codon_regex, aminoacido in diccionario.items():
            if re.match(codon_regex, codon):
                proteina += aminoacido
                break  # Se encontró una coincidencia, se sale del bucle interno
        else:
            proteina += "?"  # Codón no reconocido, se utiliza "?" como marcador
    return proteina

def main():
    if len(sys.argv) != 2:
        print('Debe ejecutarse como ./ORF_transcript.py <Secuencia>')
        sys.exit()

    secuenciaPositiva = sys.argv[1]
    stop = '(UAA|UAG|UGA|TAA|TAG|TGA)'
    secuenciaNegativa = obtener_hebra_negativa(secuenciaPositiva)

    

    # marcos de lectura hebra positiva
    for i in range(3):
        orf = funcion(secuenciaPositiva[i:], stop)
        if(orf!=[]):imprime(orf,secuenciaPositiva,'+',dict)
    # marcos de lectura hebra negativa
    for i in range(3):
        orf = funcion(secuenciaNegativa[i:], stop)
        if(orf!=[]):imprime(orf,secuenciaNegativa,'-',dict)
        
        

if __name__ == "__main__":
    main()

"""
secuencia
AGATGCCTATGGATGTTAATGATTGAGTGATATAACG
resultados
ATGTTAATGATTGAGTGA 12   18  + MLMIE
ATGCCTATGGATGTTAATGATTGA    2   24  +   MPMDVND

"""