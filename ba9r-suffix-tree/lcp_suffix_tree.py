
with open('dataset_96_5.txt','r') as f:
    text = f.readline().strip()
    suffix_array = map(int, f.readline().split(', '))
    lcp = map(int, f.readline().split(', '))

#print text
#print suffix_array
#print lcp

#text = 'GTAGT$'
#suffix_array = [5, 2, 3, 0, 4, 1]
#lcp = [0, 0, 0, 2, 0, 1]

suffix_tree = []
for i in range(len(suffix_array)-1):
    c = suffix_array[i]
    if lcp[i] == 0 and lcp[i+1] == 0:
        suffix_tree.append(text[c::])
    elif lcp[i] == 0 and lcp[i+1]>0:
        suffix_tree.append(text[c:c+lcp[i+1]])
        suffix_tree.append(text[c+lcp[i+1]:])
    elif lcp[i] > 0 and lcp[i+1] == 0:
        suffix_tree.append(text[c+lcp[i]:])
    elif lcp[i] > 0 and lcp[i+1] > 0:
        if lcp[i] == lcp[i+1]:
            suffix_tree.append(text[c+lcp[i+1]:])
        elif lcp[i] < lcp[i+1]:
            suffix_tree.append(text[c:c+lcp[i+1]])
            suffix_tree.append(text[c+lcp[i+1]:])
        elif lcp[i] > lcp[i+1]:
            suffix_tree.append(text[c+lcp[i]:])

last = suffix_array[len(suffix_array)-1]
#print last
suffix_tree.append(text[last+lcp[len(suffix_array)-1]:])

#print suffix_tree

print '\n'.join(suffix_tree)
