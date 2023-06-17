#!/bin/bash
#gff3stats.sh
#invocación: ./gff3stats.sh
#awk -v RS= '/>gi/' ORS='\n\n' codeToSplit.fasta 

#"""Esto esta comentado
#awk '/>/{ n=NR
#    while (length($n)){
#        getline linea < "codeToSplit.fasta"
#        print linea
#        n++
#    }
#    }' codeToSplit.fasta


#awk '/>/{ n=NR
#    while (length($n)){
#        print(n)
#        n++
#    }
#    }' codeToSplit.fasta
#
#count=0
#awk '/>/{ 
#    x=NR
#    if (count = 0){
#        count++
#        y = x 
#        }
#    else{
#	    | awk 'NR==3, NR==8' codeToSplit.fasta |
#        count++
#        }
#    }' codeToSplit.fasta


#| cat > doc['$count'].txt;

















lista=""
count=0
awk '/>/{ 
    x= NR
    lista = lista x
    print x
    count++
}' codeToSplit.fasta

#echo Lista
#$largo = awk '/>/{ print NR}' codeToSplit.fasta | wc -l

#for (i in Lista){
#    awk 'NR==i, NR==i-1' codeToSplit.fasta 
#}