
#pattern_list = ['GAGG','GGGG','GGGA','CAGG','AGGG','GGAG']


#with open('dataset_53_6.txt','r') as f:
#    input_k = int(f.readline().rstrip('\n'))
#    text = f.readline().rstrip('\n')

#k = input_k - 1

pattern_list = [line.strip() for line in open('dataset_54_7.txt','r')]
d = dict()

for kmer in pattern_list:
    prefix = kmer[0:len(kmer)-1]
    suffix = kmer[1:len(kmer)]
    if prefix not in d:
        d[prefix] = [suffix]
    else:
        d[prefix].append(suffix)
        

#print d
for key in sorted(d.iterkeys()):
    print "%s -> %s" % (key, ','.join(sorted(list(set(d[key])))))

# list(set(my_list)) removes duplicates in list
