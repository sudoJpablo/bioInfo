#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW, NCBIXML
import sys

def blasteando(seq):
    print("BLASTeando secuencia ...")
    resultados = NCBIWWW.qblast("blastn", "nt", seq)
    with open("resultado_blast.xml", "w") as out_handle:
        out_handle.write(resultados.read())
    resultados.close()
    return

def informacion():
    print("Obteniendo informacion del gen...")
    resultados = open("resultado_blast.xml")
    blast_record= NCBIXML.read(resultados)
    alineamiento = blast_record.alignments[0]
    
    resultados.close()
    return alineamiento.hit_id

def main():
    if(len(sys.argv) != 2):
        print("Debe ejecutarse como Blastea_e_informa.py <query>")
        sys.exit()

    my_seq = Seq(sys.argv[1])
    #blasteando(my_seq)
    gen_id = informacion()
    print(gen_id)
    

print('***archivo almacenado***')

main()
"""
Cree un programa ejecutable desde la línea de comandos,
que al ser invocado reciba como argumento una secuencia query. 
Esta secuencia deberá ser BLASTeada online. 
De los resultados obtenidos (correspondientes a alineamientos), 
el programa deberá considerar el primer HSP del primer Hit y extraer 
el identificador del gen en el cual se encuentra, 
para posteriormente descargar información sobre este gen y 
mostrar la siguiente información:

- Especie a la que pertenece
- Gen al cual pertenece, indicando:
    - cromosoma en el que se encuentra
    - Ubicación y hebra (+/-)
    - número de exones que posee el gen
"""