#!/bin/bash
#bibliografia -> https://vinuesa.github.io/intro2linux/index.html

#Entregar permisos al bash ./chmod +x splitFasta.sh
#Forma de Ejecutar ./splitFasta.sh <archivo_fasta> <directorio>
#Ejemplo ./splitFasta.sh sequenceCro16.fasta slipCro16

mkdir -p "$2"
awk -v RS=">" -v ORS='\n' -v output_dir="$2" '{
    if (NR != 1){
        n = split($0, lines, "\n")
        nombre_fasta = (NR-1) "_" substr($0, 1, 6) substr(lines[1], length(lines[1])-4)
        gsub(/[[:space:]<'"'"'"!@#$%|^&]/, "", nombre_fasta)
        print > output_dir "/" nombre_fasta ".fasta"
    }
}' "$1"
