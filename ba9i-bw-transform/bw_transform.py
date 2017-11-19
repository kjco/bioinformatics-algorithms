

#text = 'GCGTGCCTGGTCA$'

with open('dataset_97_4.txt','r') as f:
    text = f.readline().strip()

bwt_list = []
for i in range(len(text)):
    cycle = text[len(text)-i:] + text[:len(text)-i]
    bwt_list.append(cycle)
    #print cycle

bwt_list = sorted(bwt_list)


bwt = ''
for n in bwt_list:
    bwt = bwt + n[len(n)-1:]

print bwt
