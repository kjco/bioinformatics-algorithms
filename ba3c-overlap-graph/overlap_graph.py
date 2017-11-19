# Programming solution for:
#   Construct the Overlap Graph of a Collection of k-mers
#   http://rosalind.info/problems/ba3c/
# 
# In this chapter, we use the terms prefix and suffix to refer to the first k −
# 1 nucleotides and last k − 1 nucleotides of a k-mer, respectively.
# 
# Given an arbitrary collection of k-mers Patterns, we form a graph having a node
# for each k-mer in Patterns and connect k-mers Pattern and Pattern' by a
# directed edge if Suffix(Pattern) is equal to Prefix(Pattern'). The resulting
# graph is called the overlap graph on these k-mers, denoted Overlap(Patterns).
# 
# **Overlap Graph Problem**
# 
# Construct the overlap graph of a collection of k-mers.
#   - Given: A collection Patterns of k-mers.
#   - Return: The overlap graph Overlap(Patterns), in the form of an adjacency list.
#

# Sample input:
#     kmer_list = ['ATGCG','GCATG','CATGC','AGGCA','GGCAT']
kmer_list = [line.strip() for line in open('dataset_52_7.txt','r')]

d = dict()
for kmer in kmer_list:
    for alt in kmer_list:
        if kmer[1:len(kmer)] == alt[0:len(alt)-1]:
            d[kmer] = alt

for key in sorted(d.iterkeys()):
    print "%s -> %s" % (key, d[key])

