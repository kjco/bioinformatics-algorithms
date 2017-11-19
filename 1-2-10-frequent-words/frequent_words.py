# Finding the most frequent words

open_file = open('dataset_2_4.txt', 'r')
read_genome = open_file.readline().rstrip('\n')
kmer = int(open_file.readline())

open_file.close()

genome_len = len(read_genome)
pattern_dic = dict()

for i in range(genome_len - kmer):
    pattern = read_genome[i:i+kmer]
    if pattern in pattern_dic:
        pattern_dic[pattern] += 1
    else:
        pattern_dic[pattern]=1

current_max=0
pattern_list = []

for key, value in pattern_dic.iteritems():
    if value > current_max:
        current_max = value

for key, value in pattern_dic.iteritems():
    if value == current_max:
        pattern_list.append(key)

print ' '.join(pattern_list)


# Alternative code
# pattern_list = [key for key, value in pattern_dic.iteritems() if value == current_max]
