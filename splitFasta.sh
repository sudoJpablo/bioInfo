#!/bin/bash

# Comprobar si se proporcionan los argumentos necesarios
if [ $# -ne 2 ]; then
  echo "Usage: $0 <archivo_fasta> <directorio>"
  exit 1
fi

# Extraer argumentos
archivo_fasta=$1
directorio=$2

# Comprobar si el archivo FASTA existe
if [ ! -f "$archivo_fasta" ]; then
  echo "El archivo FASTA $archivo_fasta no existe."
  exit 1
fi

# Crear el directorio si no existe
if [ ! -d "$directorio" ]; then
  mkdir "$directorio"
fi

# Leer el archivo FASTA línea por línea
while IFS= read -r linea; do
  # Si es una línea de descripción de secuencia
  if [[ $linea =~ ^\>.+ ]]; then
    # Extraer los 5 primeros y últimos caracteres de la descripción
    nombre_archivo=$(echo "$linea" | awk '{print substr($0, 2, 6) substr($0, length($0)-4)}')

    # Eliminar espacios y caracteres inválidos del nombre de archivo
    nombre_archivo=$(echo "$nombre_archivo" | tr -d '[:space:]<>:"/\|?*')


    # Generar el nombre completo del archivo de salida
    archivo_salida="$directorio/$nombre_archivo.fasta"

    # Crear el archivo de salida con la línea de descripción
    echo "$linea" > "$archivo_salida"
  else
    # Agregar la línea de secuencia al archivo de salida
    echo "$linea" >> "$archivo_salida"
  fi
done < "$archivo_fasta"
