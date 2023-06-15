#!/bin/bash

# Biblio --> 
#   https://www.linuxparty.es/35-linux/11087-como-usar-el-comando-grep-en-linux-unix-con-ejemplos-practicos.html
#   https://www.solvetic.com/tutoriales/article/3871-como-guardar-resultado-comando-en-archivo-texto-linux/    
#    https://atareao.es/tutorial/scripts-en-bash/variables-en-bash/
#    https://bioinf.comav.upv.es/courses/unix/scripts_bash.html
#    https://blog.desdelinux.net/elimina-lineas-duplicadas-de-un-archivo/
#   https://www.enmimaquinafunciona.com/pregunta/64205/mostrar-el-numero-de-lineas-de-un-archivo-especifico
#

echo "Inicio Script Cuenta Exones"


#grep -oP 'ID=exon-\K[^.]+' $1 -h ./* >> exones.txt
#grep -oP ''Parametro_Inicio'\K[^'Parametro_FIN']+' $1 -h ./* >> exones.txt
grep -oP ''$2'\K[^'$3']+' $1 -h ./* >> exones.txt

cat exones.txt | sort | uniq > Sort_exones.txt
#cat tamaño_archivo1.txt | wc -l
tail -n +2 Sort_exones.txt | wc -l

rm exones.txt
rm Sort_exones.txt
echo "Fin Script"
