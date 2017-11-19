# sliding window (L,t) clumps of kmers within genome string

open_file = open('dataset_4_4.txt', 'r')
read_genome = open_file.readline().rstrip('\n')
open_file.close()


k=10
L=521
t=19
# read_genome = "CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
pattern_dic = dict()
pattern_list = []
    
genome_len = len(read_genome)


for i in range(L-k):
    pattern = read_genome[i:i+k]
    if pattern in pattern_dic:
        pattern_dic[pattern] += 1
    else:
        pattern_dic[pattern] = 1

for key,value in pattern_dic.iteritems():
    if value == t:
        pattern_list.append(key)



for j in range(genome_len - L - k):
    add_pattern = read_genome[L-k+1+j:L+1+j]
    del_pattern = read_genome[j:j+k]

    pattern_dic[del_pattern] -= 1
    if add_pattern in pattern_dic:
        pattern_dic[add_pattern] += 1
    else:
        pattern_dic[add_pattern] = 1
        
    for key, value in pattern_dic.iteritems():
        if value == t:
            pattern_list.append(key)

# print pattern_list # check pattern

pattern_list_nr = list(set(pattern_list)) # eliminates duplicates

print pattern_list_nr

print ' '.join(pattern_list_nr)
