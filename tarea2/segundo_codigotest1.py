# Partidor Degenera y secuencia 
# codigo obtenido de chatGPT3 -> Revisar

#
"""
Ejecutar como $ python3 segundo_codigotest1.py AUGUUUAUACGGAUGCCUACUGAUGUAGUCUAGUGAUCGUAA
Resustados:

"""

#!/usr/bin/env python
import sys

def find_orfs(sequence):
    start_codon = "AUG"
    stop_codons = ["UAA", "UAG", "UGA"]
    orfs = []

    for i in range(len(sequence)):
        if sequence[i:i+3] == start_codon:
            for j in range(i+3, len(sequence), 3):
                if sequence[j:j+3] in stop_codons:
                    orf = sequence[i:j+3]
                    if len(orf) % 3 == 0:
                        orfs.append(orf)
                    break

    reverse_sequence = sequence[::-1].replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c").upper()
    for i in range(len(reverse_sequence)):
        if reverse_sequence[i:i+3] == start_codon:
            for j in range(i+3, len(reverse_sequence), 3):
                if reverse_sequence[j:j+3] in stop_codons:
                    orf = reverse_sequence[i:j+3][::-1]
                    if len(orf) % 3 == 0:
                        orfs.append(orf)
                    break

    return orfs

def translate_sequence(sequence):
    codon_table = {
        "AUG": "M", "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "UAU": "Y",
        "UAC": "Y", "UGU": "C", "UGC": "C", "UGG": "W", "CUU": "L",
        "CUC": "L", "CUA": "L", "CUG": "L", "CCU": "P", "CCC": "P",
        "CCA": "P", "CCG": "P", "CAU": "H", "CAC": "H", "CAA": "Q",
        "CAG": "Q", "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "ACU": "T", "ACC": "T",
        "ACA": "T", "ACG": "T", "AAU": "N", "AAC": "N", "AAA": "K",
        "AAG": "K", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V", "GCU": "A",
        "GCC": "A", "GCA": "A", "GCG": "A", "GAU": "D", "GAC": "D",
        "GAA": "E", "GAG": "E", "GGU": "G", "GGC": "G", "GGA": "G",
        "GGG": "G"
    }

    protein_sequence = ""
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        amino_acid = codon_table.get(codon, "")
        if amino_acid:
            protein_sequence += amino_acid

    return protein_sequence

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python orf_finder.py <sequence>")
        sys.exit(1)

    sequence = sys.argv[1].upper()
    orfs = find_orfs(sequence)

    print("ORFs:")
    for orf in orfs:
        print(orf)

    print("\nProtein Sequences:")
    for orf in orfs:
        protein_sequence = translate_sequence(orf)
        print(protein_sequence)