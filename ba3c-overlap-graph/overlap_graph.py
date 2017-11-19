


#kmer_list = ['ATGCG','GCATG','CATGC','AGGCA','GGCAT']

kmer_list = [line.strip() for line in open('dataset_52_7.txt','r')]

d = dict()
for kmer in kmer_list:
    for alt in kmer_list:
        if kmer[1:len(kmer)] == alt[0:len(alt)-1]:
            d[kmer] = alt

for key in sorted(d.iterkeys()):
    print "%s -> %s" % (key, d[key])

#print d
