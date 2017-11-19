

def comp_string(text,k):
    comp_list = []
    for i in range(len(text)-k+1):
        comp = text[i:i+k]
        comp_list.append(comp)
    lex_comp_list = sorted(comp_list)
    return lex_comp_list
    
#input_text = 'AAGATTCTCTAC'
#input_k = 3

with open('dataset_53_6.txt','r') as f:
    input_k = int(f.readline().rstrip('\n'))
    input_text = f.readline().rstrip('\n')

#print comp_string(input_text,input_k)

#kmer_list = [line.strip() for line in open('dataset_52_7.txt','r')]

kmer_list = comp_string(input_text,input_k-1)
d = dict()

for kmer in kmer_list:
    v_list = []
    for alt in kmer_list:
        if kmer[1:len(kmer)] == alt[0:len(alt)-1]:
            v_list.append(alt)
            d[kmer] = v_list


for key in sorted(d.iterkeys()):
    print "%s -> %s" % (key, ','.join(sorted(list(set(d[key])))))

# list(set(my_list)) removes duplicates in list
