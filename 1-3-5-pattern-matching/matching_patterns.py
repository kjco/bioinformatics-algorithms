# Pattern Matching Problem; Find index of patterns in a string

open_file = open('dataset_3_5.txt', 'r')
read_pattern = open_file.readline().rstrip('\n')
read_genome = open_file.readline()

open_file.close()

pattern_len = len(read_pattern)
genome_len = len(read_genome)

print read_pattern
print pattern_len
print genome_len

output_file = []

for i in range(genome_len - pattern_len):
    if read_pattern == read_genome[i:i+pattern_len]:
        output_file.append(str(i))


print ' '.join(output_file)
