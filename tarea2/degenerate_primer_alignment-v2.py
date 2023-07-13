#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Partidor Degenera y secuencia 
"""
#Tarea 2 
#Grupo 
- Andrade   , Jorge       - jorge.andrade01@alumnos.uach.cl 
- Fuentes   , Sebastian   - sebastian.fuentes02@alumnos.uach.cl 
- Pezo      , Juan Pablo  - juan.pezo@alumnos.uach.cl 
- Pinilla   , Claudio     - claudio.pinilla@alumnos.uach.cl
"""
import sys
import re
import argparse
# Ej: $ python3 degenerate_primer_alignment-v2.py TGCATGCCGATGCGATACGATACGGCGATAC RGCAT
#

#symbolDic es el diccionario que contiene los codigos de cada partidor, para asi formar la expresion regular
#En el caso del partidor ser S, entonces el codigo seria [GC] lo que quiere decir que es o G o C
symbolDic = dict()
symbolDic = {
    'A': 'A',
    'C': 'C',
    'G': 'G',
    'T': 'T',
    'R': '[AG]',
    'Y': '[CT]',
    'S': '[GC]',
    'W': '[AT]',
    'K': '[GT]',
    'M': '[AC]',
    'B': '[CGT]',
    'D': '[AGT]',
    'H': '[ACT]',
    'V': '[ACG]',
    'N': '[ACGT]'
}

def main():

    if(len(sys.argv)!=3):
        print('Debe ejecutarse como $python3 degenerate_primer_alignment-v2.py <Secuencia ADN> <Partidor Degenerado>')
        sys.exit()

    parser = argparse.ArgumentParser()
    parser.add_argument('sequence')
    parser.add_argument('primer')
    args = parser.parse_args()

    positions = find_matching_positions(args.sequence, args.primer)
    if positions:
        print("pos\t seq")
        for start, end, aligned_sequence in positions:
            print(f"{start}\t{aligned_sequence}")
    else:
        print("No se encontraron coincidencias.")

def find_matching_positions(sequence, primer):
    pattern = ''.join([symbolDic.get(base, base) for base in primer])
    regex = re.compile(pattern)
    matches = [(m.start(), m.end(), sequence[m.start():m.end()]) for m in regex.finditer(sequence)]
    return matches

if __name__ == '__main__':
    main()