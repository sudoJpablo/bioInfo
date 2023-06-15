#!/bin/bash
#gff3stats.sh
#invocación: ./gff3stats.sh

file_path=$1
region_name=""
gene_name=""
exon_count=0
cds_count=0
exones=()

while IFS=$'\t' read -r -a fields; do
    if [[ ! ${fields[0]} =~ ^# ]]; then
        feature_type=${fields[2]}
        attributes=${fields[8]}
        IFS=';' read -r -a attribute_list <<< "$attributes"

        if [[ $feature_type == "region" ]]; then
            for attribute in "${attribute_list[@]}"; do
                if [[ $attribute == Name=* ]]; then
                    region_name=${attribute#*=}
                    break
                fi
            done
        elif [[ $feature_type == "gene" ]]; then
            for attribute in "${attribute_list[@]}"; do
                if [[ $attribute == Name=* ]]; then
                    gene_name=${attribute#*=}
                    break
                fi
            done
        elif [[ $feature_type == "exon" ]]; then
            ((exon_count++))
        elif [[ $feature_type == "CDS" ]]; then
            ((cds_count++))
        fi
        #INICIO PARTE AGREGADA PARA TEST

        #FIN PARTE AGREGADA PARA TEST
    fi
done < "$file_path"
##

while IFS=$'\t' read -r fields; do
    if [[ "$tipo_feature" == "exon" ]]; then
      id=$(grep -oP 'ID=exon-\K[^.]+' <<< "$contenido_info")
      if [[ ! " ${exones[@]} " =~ " ${id} " ]]; then
        exones+=("$id")
      fi
    fi
done < "$archivo"

echo "Cantidad de exones diferentes: ${#exones[@]}"
echo "Lista de exones diferentes:"
for exon in "${exones[@]}"; do
    echo "- $exon"
done
##
echo "Largo de la lista de objetos diferentes: ${#exones[@]}"
echo "----------------------------------------------------"

echo "$region_name"
echo "$gene_name"
echo "$exon_count"
echo "$cds_count"