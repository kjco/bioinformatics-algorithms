# Programming solution for: 
#   Generate the k-mer Composition of a String
#   http://rosalind.info/problems/ba3a/
#
# Given a string Text, its k-mer composition Compositionk(Text) is the
# collection of all k-mer substrings of Text (including repeated k-mers). For
# example,
#     Composition4(TATGGGGTGC) = {ATG, GGG, GGG, GGT, GTG, TAT, TGC, TGG}
#
# Note that we have listed k-mers in lexicographic order (i.e., how they would
# appear in a dictionary) rather than in the order of their appearance in
# TATGGGGTGC. We have done this because the correct ordering of the reads is
# unknown when they are generated.
# 
# **String Composition Problem**
# 
# Generate the k-mer composition of a string.
#   - Given: An integer k and a string Text.
#   - Return: Compositionk(Text) (the k-mers can be provided in any order).
#

# Sampleinput:
#     k =5
#     text = 'CAATCCAAC'

with open('dataset_51_3.txt','r') as f:
    k = int(f.readline().rstrip('\n'))
    text = f.readline().rstrip('\n')

comp_list = []

for i in range(len(text)-k+1):
    comp = text[i:i+k]
    comp_list.append(comp)

lex_comp_list = sorted(comp_list)

print '\n'.join(lex_comp_list)

