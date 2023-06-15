#!/bin/bash

# Biblio --> 
#    https://atareao.es/tutorial/scripts-en-bash/variables-en-bash/
#    https://bioinf.comav.upv.es/courses/unix/scripts_bash.html
#    https://blog.desdelinux.net/elimina-lineas-duplicadas-de-un-archivo/
#   https://www.enmimaquinafunciona.com/pregunta/64205/mostrar-el-numero-de-lineas-de-un-archivo-especifico
#


#grep -oP 'ID=NG_\K[^.]+' $1 
grep -oP 'ID=NC_\K[^.]+' $1
grep -oP 'ID=gene-\K[^;]+' $1 | head -n 1 
#grep -oP 'ID=id-\K[^-]+' $1

#grep -oP ''$4'\K[^'$5']+' $1
#grep -oP 'ID=gene-\K[^;]+' $1


#grep -oP ''Parametro_Inicio'\K[^'Parametro_FIN']+' $1 -h ./* >> exones.txt
#grep -oP ''$2'\K[^'$3']+' $1 -h ./* >> exones.txt
