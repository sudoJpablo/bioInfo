#!/bin/bash
# Programa main de extraccion Informacion gff3 y otros

grep -oP 'Name=\K[^\n]+' $1 && grep -oP 'region\K[^\n]+' $1 | cut -d " " -f2 && grep -oP 'exon\K[^.]+' $1 | sort | uniq  | cat | wc -l && grep -oP 'ID=cds\K[^;]+' $1 | sort | uniq  | cat | wc -l
