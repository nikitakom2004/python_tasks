# двоичное кодирование нуклеотидов ДНК
def encode_bin(dna):
    # словарь для кодирования в бинарный код
    tr = {'A': '00', 'T': '11', 'G': '10', 'C': '01'}
    out = ''
    for p in dna:
        out += tr[p]

    return out


# транскрипция ДНК в РНК
# Adenine(A), Thymine(T), Guanine(G), Cytosine(C) - ДНК
# Adenine (A), Cytosine (C), Guanine (G), Uracil (U) - РНК
# G –> C
# C –> G
# T –> A
# A –> U
def transcript(dna):
    # словарь транскрипции в РНК
    tr = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    out = ''
    for p in dna:
        out += tr[p]

    return out


# трансляция
#   A   Ala   Alanine          Аланин
#   R   Arg   Arginine         Аргинин
#   N   Asn   Asparagine       Аспарагин
#   D   Asp   Aspartic Acid    Аспарагиновая кислота
#   C   Cys   Cysteine         Цистеин
#   Q   Gln   Glutamine        Глютамин
#   E   Glu   Glutamic Acid    Глютаминовая кислота
#   G   Gly   Glycine          Глицин
#   H   His   Histidine        Гистидин
#   I   Ile   Isoleucine       Изолейцин
#   L   Leu   Leucine          Лейцин
#   K   Lys   Lysine           Лизин
#   M   Met   Methionine       Метионин
#   F   Phe   Phenylalanine    Фенилаланин
#   P   Pro   Proline          Пролин
#   S   Ser   Serine           Серин
#   T   Thr   Threonine        Треонин
#   W   Trp   Thryptophan      Триптофан
#   Y   Tyr   Tyrosine         Тирозин
#   V   Val   Valine           Валин

def translate(seq):
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }
    protein = ''
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein += table[codon]
    return protein


def protein_rus(seq):
    table = {'A': 'Аланин',
    'R': 'Аргинин',
    'N': 'Аспарагин',
    'D': 'Аспарагиновая кислота',
    'C': 'Цистеин',
    'Q': 'Глютамин',
    'E': 'Глютаминовая кислота',
    'G': 'Глицин',
    'H': 'Гистидин',
    'I': 'Изолейцин',
    'L': 'Лейцин',
    'K': 'Лизин',
    'M': 'Метионин',
    'F': 'Фенилаланин',
    'P': 'Пролин',
    'S': 'Серин',
    'T': 'Треонин',
    'W': 'Триптофан',
    'Y': 'Тирозин',
    'V': 'Валин',
    '_': '_'}

    out = ''
    for p in seq:
        out += table[p]
        out += ' '

    return out


def verify(sequence):
    # превращаем строку в множество уникальных значений
    seq = set(sequence)

    # проверим является ли полученное множество подмножеством всех нуклеотидов ДНК
    if seq.issubset({'A', 'T', 'C', 'G'}):
        return True

    return False

if __name__ == '__main__':

    dna = 'GGTCAGAAAAAGCCCTCTCCATGTCTACTCACGATACATCCCTGAAAACCACTGAGGAAGTGGCTTTTCAGA'

    # проверяем входную последовательность на соответствие ДНК
    if verify(dna):
        # транскриация ДНК->РНК
        print(transcript(dna))

        # трансляция
        print(protein_rus(translate(dna)))

        # двоичное кодирование ДНК
        print(encode_bin('GGC'))
