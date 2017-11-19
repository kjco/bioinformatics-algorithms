# Find a string within a larger sequence with tolerance to mismatches d

# a is pattern string (constant); b will be strings of genome to compare (dynamic)

def compare_func(a,b):
    string_len = len(a)
    count = 0
    for i in range(string_len):
        if a[i] != b[i]:
            count += 1
    return count
            

open_file = open('dataset_8_3.txt', 'r')
read_pattern = open_file.readline().rstrip('\n')
read_genome = open_file.readline().rstrip('\n')
mismatches = int(open_file.readline())  #int() converts to integer

open_file.close()

pattern_len = len(read_pattern)
genome_len = len(read_genome)

print read_pattern
print pattern_len
print genome_len
print mismatches

output_file = []

for k in range(genome_len - pattern_len + 1):
    genome_seq = read_genome[k:k+pattern_len]
    mismatch_num = compare_func(read_pattern,genome_seq)
    if mismatch_num <= mismatches:
        output_file.append(str(k))

print ' '.join(output_file)



