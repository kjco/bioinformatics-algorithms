# minimum skew


open_file = open('dataset_7_6.txt', 'r')
read_genome = open_file.readline().rstrip('\n')

open_file.close()

genome_len = len(read_genome)

count = 0
min_skew =2
locations = []

for i in range(genome_len):
    if read_genome[i]=="C":
        count -= 1
    elif read_genome[i]=="G":
        count += 1
    if count < min_skew:
        min_skew=count
        locations=[]
        locations.append(str(i+1))
    elif count == min_skew:
        locations.append(str(i+1))

print ' '.join(locations)
    

          
