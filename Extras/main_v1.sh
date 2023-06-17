#!/bin/bash
# Programa main de extraccion Informacion gff3 y otros

#para ejecutar: ./main.sh <Parametro1_Ruta> <parametros2_Estructura>

file_path=$1
exon_filter1=$2
exon_filter2=$3
cds_filter1=$4
cds_filter2=$5

#Ejecutar Leer NombreGEN
    #cd function/
    #./read_Region.sh ../$2
#FIN Ejecucion Leer NombreGEN

echo Lectura de Exones
echo Requiero los parametros_1 "Inicio" y Parametro_2 "Fin" 
echo El Patron del ID Exon se Encuentra entre estos parametros
echo Parametro_1
read varname1
echo Parametro_2
read varname2

#Ejecutar Cuenta Exones
cd function/
#./Exon_Count.sh ../sequence.gff3 ID=exon- .
./Exon_Count.sh ../$1 $varname1 $varname2
#FIN Ejecucion Cuenta Exones

echo Lectura de CDS
echo Requiero los parametros_1 "Inicio" y Parametro_2 "Fin" 
echo El Patron del ID CDS se Encuentra entre estos parametros
echo Parametro_1
read varname3
echo Parametro_2
read varname4

#Ejecutar Cuenta Exones
cd function/
#./Exon_Count.sh ../sequence.gff3 ID=exon- .
./Exon_Count.sh ../$1 $varname3 $varname4
#FIN Ejecucion Cuenta Exones
