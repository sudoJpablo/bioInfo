# Partidor Degenera y secuencia 
# codigo obtenido de chatGPT3 -> Revisar

"""
TEST 1
Ejecutar como $ python3 primer_codigotest1.py ATCGATCGATCGATCGATCG ATNGAT
Seq : ATCGATCGATCGATCGATCG ATNGAT
coincidencias]
0 6
Con solapamiento
4 10
8 14
12 18 
16 22
20 26

"""
import re
import argparse

IUPAC_CODES = {
    'A': 'A',
    'C': 'C',
    'G': 'G',
    'T': 'T',
    'R': '[AG]',
    'Y': '[CT]',
    'S': '[GC]',
    'W': '[AT]',
    'K': '[GT]',
    'M': '[AC]',
    'B': '[CGT]',
    'D': '[AGT]',
    'H': '[ACT]',
    'V': '[ACG]',
    'N': '[ACGT]'
}

def find_matching_positions(sequence, primer):
    pattern = ''.join([IUPAC_CODES.get(base, base) for base in primer])
    regex = re.compile(pattern)
    return [(m.start(), m.end()) for m in regex.finditer(sequence)]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('sequence')
    parser.add_argument('primer')
    args = parser.parse_args()

    positions = find_matching_positions(args.sequence, args.primer)
    if positions:
        for start, end in positions:
            print(f"Start: {start}, End: {end}")
    else:
        print("No matches found.")

if __name__ == '__main__':
    main()