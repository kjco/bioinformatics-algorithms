

#text = 'AAGATTCTCTAC'
#input_k = 4

with open('dataset_53_6.txt','r') as f:
    input_k = int(f.readline().rstrip('\n'))
    text = f.readline().rstrip('\n')

k = input_k - 1
d = dict()

for i in range(len(text)-k):
    prefix = text[i:i+k]
    suffix = text[i+1:i+k+1]
    if prefix not in d:
        d[prefix] = [suffix]
    else:
        d[prefix].append(suffix)
        

#print d
for key in sorted(d.iterkeys()):
    print "%s -> %s" % (key, ','.join(sorted(list(set(d[key])))))

# list(set(my_list)) removes duplicates in list
