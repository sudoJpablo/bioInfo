#!/bin/bash
#gff3stats.sh
#invocación: ./gff3stats.sh

file_path=$1
region_name=""
gene_name=""
exon_count=0
cds_count=0

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
    fi
done < "$file_path"

echo "$region_name"
echo "$gene_name"
echo "$exon_count"
echo "$cds_count"