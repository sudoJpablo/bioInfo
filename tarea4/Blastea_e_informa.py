#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW, NCBIXML
from Bio import Entrez
from Bio import SeqIO
import sys

def blasteando(seq):
    print("BLASTeando secuencia ...")
    resultados = NCBIWWW.qblast("blastn", "nt", seq)
    with open("resultado_blast.xml", "w") as out_handle:
        out_handle.write(resultados.read())
    resultados.close()
    print('***archivo almacenado***')
    return

def informacion():
    print("Obteniendo informacion del gen...")
    resultados = open("resultado_blast.xml")
    blast_record= NCBIXML.read(resultados)      #gi|71143213|gb|AC165171.2|
    alineamiento = blast_record.alignments[0]   #0123456789
    partes = alineamiento.hit_id.split('|')
    id = partes[3].split('.')
    resultados.close()
    return id[0]
    

def accediendoNCBI(id_gen):
    Entrez.email = "micorreo@uach.cl"

    with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=id_gen) as handle:
        seq_record = SeqIO.read(handle, "gb")

        print(f"Especie: {seq_record.annotations['organism']}")
        print(f"Indentificador del gen: {seq_record.annotations['accessions'][0]}")
        print(f"Ubicacion: {seq_record.features[0].location}")
        
        c=0
        for i in seq_record.features:
            if(i.type == 'exon'):
                c+=1
        print(f"Exones en el gen: {c}")
    
    return

def main():
    if(len(sys.argv) != 2):
        print("Debe ejecutarse como Blastea_e_informa.py <query>")
        sys.exit()

    my_seq = Seq(sys.argv[1])
    #blasteando(my_seq)
    gen_id = informacion()
    accediendoNCBI(gen_id)


main()
