#!/bin/bash


#grep -oP ''$2'\K[^'$3']+' $1 | cat | wc -l

grep -oP ''$2'\K[^'$3']+' $1 | sort | uniq  | cat | wc -l


#Codigo antiguo
#grep -oP ''$2'\K[^'$3']+' $1 -h ./* >> exones.txt

#cat exones.txt | sort | uniq > Sort_exones.txt
#cat Sort_exones.txt | wc -l

#rm exones.txt
#rm Sort_exones.txt
