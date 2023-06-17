#!/bin/bash
# Programa main de extraccion Informacion gff3 y otros
#Para distintos gff3
#./main.sh sequence.gff3 ID=NG_ ID=gene- ID=exon- ID=cds-NP_ . .
#./main.sh eden1.gff3 -region Name= exon ID=cds Parent Parent

#para ejecutar: ./main.sh <Parametro1_file> <parametros2_region>  <Parametro3_gen> <parametros4_exon> <parametros5_CDS> 

file_path=$1
#region_filter=$2
#region_filterFin=$3
#nameGen_filter=$4
#nameGen_filterFin=$5
#exon_filter1=$6
#exon_filter1Fin=$7
#cds_filter1=$8
#cds_filter1Fin=$9

#echo "'$1','$2', '$3','$4','$5','$6','$7','$8','$9'"
cd function/
#./second_bestFunctionBeta.sh ../$1 $2 $3 $4 $5
#./second_bestFunctionBeta.sh ../$1 $2 $3
#./second_bestFunctionBeta.sh ../$1 $4 $5
./second_bestFunctionBeta.sh ../$1
./bestFunctionBeta.sh ../$1  ID=exon- .
./bestFunctionBeta.sh ../$1 ID=cds- .

