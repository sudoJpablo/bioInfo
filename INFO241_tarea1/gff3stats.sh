#!/bin/bash

#Entregar permisos al bash ./chmod +x gff3stats.sh
#Forma de Ejecutar ./gff3stats.sh <archivo_gff3>
#Ejemplo ./gff3stats.sh EDEN.gff3

grep -oP 'Name=\K[^\n]+' $1 && grep -oP 'region\K[^\n]+' $1 | cut -d " " -f2 && grep -oP 'exon\K[^.]+' $1 | sort | uniq  | cat | wc -l && grep -oP 'ID=cds\K[^;]+' $1 | sort | uniq  | cat | wc -l
