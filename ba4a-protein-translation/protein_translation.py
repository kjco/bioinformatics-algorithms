# Programming solution for:
#   Translate an RNA String into an Amino Acid String
#   http://rosalind.info/problems/ba4a/
#
# Much like replication, the chemical machinery underlying transcription and
# translation is fascinating, but from a computational perspective, both
# processes are straightforward. Transcription simply transforms a DNA string
# into an RNA string by replacing all occurrences of "T" with "U". The
# resulting strand of RNA is translated into an amino acid sequence via the
# genetic code; this process converts each 3-mer of RNA, called a codon, into
# one of 20 amino acids.
#
# As illustrated in Figure 1, each of the 64 RNA codons encodes its own amino
# acid (some codons encode the same amino acid), with the exception of three stop
# codons that do not translate into amino acids and serve to halt translation.
# For example, the DNA string "TATACGAAA" transcribes into the RNA string
# "UAUACGAAA", which in turn translates into the amino acid string "Tyr-Thr-Lys".
#
# The following problem asks you to find the translation of an RNA string into an
# amino acid string.
#
# Protein Translation Problem
#
# Translate an RNA string into an amino acid string.
#   - Given: An RNA string Pattern.
#   - Return: The translation of Pattern into an amino acid string Peptide.

codon_dict = {"AAA":"K","AAC":"N","AAG":"K","AAU":"N","ACA":"T","ACC":"T","ACG":"T","ACU":"T","AGA":"R","AGC":"S","AGG":"R","AGU":"S","AUA":"I","AUC":"I","AUG":"M","AUU":"I","CAA":"Q","CAC":"H","CAG":"Q","CAU":"H","CCA":"P","CCC":"P","CCG":"P","CCU":"P","CGA":"R","CGC":"R","CGG":"R","CGU":"R","CUA":"L","CUC":"L","CUG":"L","CUU":"L","GAA":"E","GAC":"D","GAG":"E","GAU":"D","GCA":"A","GCC":"A","GCG":"A","GCU":"A","GGA":"G","GGC":"G","GGG":"G","GGU":"G","GUA":"V","GUC":"V","GUG":"V","GUU":"V","UAA":"","UAC":"Y","UAG":"","UAU":"Y","UCA":"S","UCC":"S","UCG":"S","UCU":"S","UGA":"","UGC":"C","UGG":"W","UGU":"C","UUA":"L","UUC":"F","UUG":"L","UUU":"F"}
amino_acid_list = []

open_file = open('dataset_18_3.txt', 'r')
rna_string = open_file.readline().rstrip('\n')
open_file.close()

#rna_string = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
rna_string_len = len(rna_string)

for i in range(rna_string_len/3):
    codons = rna_string[3*i:3*i+3]
    amino_acid = codon_dict[codons]
    amino_acid_list.append(amino_acid)

print amino_acid_list
print ''.join(amino_acid_list)

    
