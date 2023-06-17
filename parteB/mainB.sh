#!/bin/bash
#bibliografia -> https://vinuesa.github.io/intro2linux/index.html
#El codigo se ejecuta ./ <Directorio_nuevo> <Codigo.fasta>
#Ejemplo ./ <Directorio_nuevo> <Codigo.fasta>

rm -r test4/
echo "directorio removido exitosamente"
mkdir -p "$1"
#Version1
#awk  -v RS= -v  ORS='\n\n' '{ print > "'"$1"'/seq" NR ".fasta" }' "$2"

#Version2
#awk -v RS= -v ORS="" '{
#    nombre_fasta =  substr($1, 1, 5) substr($1, length($1) - 4) 'NR'
#    gsub(/[[:space:]<>'"'"'"!@#$%|^&]/, "", nombre_fasta)
#    print > "'"$1"'/" nombre_fasta ".fasta"
#}' "$2"

#Version3
#awk -v RS=">" -v  ORS='\n' '{
#    n = split($0, lines, "\n")
#    nombre_fasta =  substr($0, 1, 6) substr(lines[1], length(lines[1])-4)
#    print lines[1]
#    gsub(/[[:space:]<'"'"'"!@#$%|^&]/, "", nombre_fasta)
#    print > "'"$1"'/" nombre_fasta ".fasta"
#}' "$2"

#Imprime sublineas de cada parrafo(si se elimina el n=split no se define lines y da error)
#version4
awk -v RS=">" -v ORS='\n' -v output_dir="$1" '{
    if (NR != 1){
        n = split($0, lines, "\n")
        print lines[1]
        nombre_fasta = (NR-1) "_" substr($0, 1, 6) substr(lines[1], length(lines[1])-4)
        gsub(/[[:space:]<'"'"'"!@#$%|^&]/, "", nombre_fasta)
        print > output_dir "/" nombre_fasta ".fasta"
    }
}' "$2"
