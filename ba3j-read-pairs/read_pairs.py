# Programming solution for:
#   Reconstruct a String from its Paired Composition
#   http://rosalind.info/problems/ba3j
# Since increasing read length presents a difficult experimental problem,
# biologists have suggested an indirect way of increasing read length by
# generating read-pairs, which are pairs of reads separated by a fixed distance
# d in the genome.
# 
# You can think about a read-pair as a long "gapped" read of length k + d + k
# whose first and last k-mers are known but whose middle segment of length d is
# unknown. Nevertheless, read-pairs contain more information than k-mers alone,
# and so we should be able to use them to improve our assemblies. If only you
# could infer the nucleotides in the middle segment of a read-pair, you would
# immediately increase the read length from k to 2 * k + d.
# 
# Given a string Text, a (k,d)-mer is a pair of k-mers in Text separated by
# distance d. We use the notation (Pattern1|Pattern2) to refer to a a (k,d)-mer
# whose k-mers are Pattern1 and Pattern2. The (k,d)-mer composition of Text,
# denoted PairedCompositionk,d(Text), is the collection of all (k,d)- mers in
# Text (including repeated (k,d)-mers).
#
# **String Reconstruction from Read-Pairs Problem**
# 
# Reconstruct a string from its paired composition.
#   - Given: Integers k and d followed by a collection of paired k-mers PairedReads.
#   - Return: A string Text with (k, d)-mer composition equal to PairedReads. (If
#     multiple answers exist, you may return any one.)


#pattern_list = ['GAGA|TTGA','TCGT|GATG','CGTG|ATGT','TGGT|TGAG','GTGA|TGTT','GTGG|GTGA','TGAG|GTTG','GGTC|GAGA','GTCG|AGAT']
pattern_list = [line.strip() for line in open('dataset_58_14.txt','r')]

d = dict()

dlen = 300
klen = (len(pattern_list[0])-1)/2
print klen

for kmer in pattern_list:
    prefix = kmer[0:klen-1] + '|' + kmer[-klen:-1]
    suffix = kmer[1:klen] + '|' + kmer[len(kmer)-klen+1:len(kmer)]
    if prefix not in d:
        d[prefix] = [suffix]
    else:
        d[prefix].append(suffix)

def out_node(input,new_input):
    for k,v in input.iteritems():
        if k not in new_input:
            return k
        elif len(input[k]) > new_input[k]:
            return k

def in_node(input, new_input):
    for k,v in new_input.iteritems():
        if k not in input:
            return k
        elif len(input[k]) < new_input[k]:
            return k

in_d = dict()

for k,v in d.iteritems():
    for node in v:
        if node not in in_d:
            in_d[node] = 1
        elif node in in_d:
            in_d[node] += 1

last_node = in_node(d, in_d)
first_node = out_node(d, in_d)
#print in_node(d, in_d)
#print out_node(d, in_d)

if last_node in d:
    d[last_node].append(first_node)
else:
    d[last_node] = [first_node]


def decide(input):
    for k,v in input.iteritems():
        if v:
            return True
    return False

cycle =[]
new_cycle = []
k = last_node
# need to assign a random key in dictionary to k (k = random key) to initiate while loop

while decide(d):
    for i in range(len(cycle)):
        if d[cycle[i]]:
            k = cycle[i]
            new_cycle = cycle[i:len(cycle)]+cycle[0:i]
            break
    ki = k
    cycle = [ki]
    while True:
        orig_k = k
        k = d[k][0]
        d[orig_k].remove(d[orig_k][0])
        if k == ki:
            break
        cycle.append(k)

    cycle = new_cycle + cycle

#break_point = None
for i in range(len(cycle)-1):
    if cycle[i] == last_node and cycle[i+1] == first_node:
        break_point = i

output_cycle = cycle[break_point+1:]+cycle[:break_point+1]
#print output_cycle

string = ''
alt_string = ''
for n in output_cycle:
    string = string + n[0]
    alt_string = alt_string + n[-1]

print string
print '====='
print alt_string
print '====='
#print alt_string[len(alt_string)-2*klen:len(alt_string)]
print string + alt_string[len(alt_string)-2*klen-dlen+2:len(alt_string)]

