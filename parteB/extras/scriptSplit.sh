#!/bin/bash
#Biblio
#   -> https://vinuesa.github.io/intro2linux/index.html

lista=()

# Agregar elementos a la lista
lista+=("elemento1")
lista+=("elemento2")
lista+=("elemento3")
count=0
awk '/>/{ 
    x = NR
    print NR
    lista+=("elemento232")
    lista+=("elemento43")   
    count++
}' codeToSplit.fasta   

# Imprimir la lista
echo "Lista completa: ${lista[@]}"

