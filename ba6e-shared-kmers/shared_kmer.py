
with open('dataset_90_2.txt','r') as f:
    kmer = int(f.readline().strip())
    str1 = f.readline().strip()
    str2 = f.readline().strip()


##kmer = 3
##str1 = 'AAACTCATCAAA'
##str2 = 'TTTCAAATC'

d = dict()

##for i in range(len(str1)-kmer+1):
##    d[str1[i:i+kmer]] = i

for i in range(len(str1)-kmer+1):
    if str1[i:i+kmer] not in d:
        d[str1[i:i+kmer]] = [i]
    elif str1[i:i+kmer] in d:
        d[str1[i:i+kmer]].append(i)
        


#print d

# function for returning reverse complement of a string
def rev_comp(string):
    rc_d = {'A':'T','C':'G','T':'A','G':'C'}
    rc_out = ''
    r_string = string[::-1]
    for i in r_string:
        rc_out = rc_out + rc_d[i]

    return rc_out
   
shared_list = []

for j in range(len(str2)-kmer+1):
    if str2[j:j+kmer] in d:
        str1_index = d[str2[j:j+kmer]]
        str2_index = j
        for n in str1_index:
            shared_list.append((n,str2_index))

    if str2[j:j+kmer] == rev_comp(str2[j:j+kmer]):
        continue

    if rev_comp(str2[j:j+kmer]) in d:
        r1_index = d[rev_comp(str2[j:j+kmer])]
        r2_index = j
        for m in r1_index:
            shared_list.append((m,r2_index))

#print shared_list

print '\n'.join('(%s, %s)' % tup for tup in shared_list)


