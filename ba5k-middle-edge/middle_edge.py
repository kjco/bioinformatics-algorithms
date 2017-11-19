import sys

# 0: down, 1: right, 2: lower right
sigma = 5

# Read the scoring matrix
d = dict()
with open('BLOSUM62.txt') as f:
    alphabets = f.readline().strip().split()

    for line in f:
        chars = line.strip().split()
        m = chars[0]
        scores = map(int, chars[1:])
        for i in range(len(scores)):
            d[(m, alphabets[i])] = scores[i]

#print d

with open('dataset_79_12.txt','r') as f:
    str2 = f.readline().strip()
    str1 = f.readline().strip()

##str2 = 'PLEASANTLY'
##str1 = 'MEASNLY'

##print len(str1)/2
##print len(str2)/2

rev1 = str1[len(str1):len(str1)/2-1:-1]
rev2 = str2[::-1]

# Initialize the matrix
m = [[0 for i in range(len(str1)/2+1)] for j in range(len(str2)+1)]
b = [[0 for i in range(len(str1)/2+1)] for j in range(len(str2)+1)]

r = [[0 for i in range(len(rev1)+1)] for j in range(len(rev2)+1)]
br = [[0 for i in range(len(rev1)+1)] for j in range(len(rev2)+1)]
# m = [ [0] * (len(str2)+1) ] * (len(str1)+1)
# b = [ [0] * (len(str2)+1) ] * (len(str1)+1)

#print m

for i in xrange(1,len(str2)+1):
    m[i][0] = -sigma*i

for j in xrange(1,len(str1)/2+1):
    m[0][j] = -sigma*j

for i in xrange(1,len(rev2)+1):
    r[i][0] = -sigma*i

for j in xrange(1,len(rev1)+1):
    r[0][j] = -sigma*j
 
#print r
#print m
#print 'matrix is %dx%d' % (len(m), len(m[0]))

for i in xrange(1, len(str2)+1):
    for j in xrange(1, len(str1)/2+1):
        m[i][j] = m[i-1][j] - sigma
        b[i][j] = 0

        if m[i][j-1] - sigma > m[i][j]:
            m[i][j] = m[i][j-1] - sigma
            b[i][j] = 1

        score =  m[i-1][j-1] + d[(str2[i-1], str1[j-1])]
        # print str1[i-1], str2[j-1], d[(str1[i-1], str2[j-1])]
        if score > m[i][j]:
            m[i][j] = score
            b[i][j] = 2

        #print i,j, m[i][j], b[i][j]

#print b
#print m[len(str1)][len(str2)]
#print m

mid_list = []
for j in range(len(str2)+1):
    mid_list.append(m[j][len(str1)/2])

#print mid_list


for i in xrange(1, len(rev2)+1):
    for j in xrange(1, len(rev1)+1):
        r[i][j] = r[i-1][j] - sigma
        br[i][j] = 0

        if r[i][j-1] - sigma > r[i][j]:
            r[i][j] = r[i][j-1] - sigma
            br[i][j] = 1

        score =  r[i-1][j-1] + d[(rev2[i-1], rev1[j-1])]
        # print [i-1], str2[j-1], d[(str1[i-1], str2[j-1])]
        if score > r[i][j]:
            r[i][j] = score
            br[i][j] = 2

r_mid_list = []
for j in range(len(rev2)+1):
    r_mid_list.append(r[j][len(rev1)])

#print r
#print r_mid_list
rev_mid_list = r_mid_list[::-1]
#print rev_mid_list

sum_list = []
for i in range(len(mid_list)):
    sum_list.append(mid_list[i]+rev_mid_list[i])

#print sum_list

max_index = sum_list.index(max(sum_list))
#print max_index

#print br
print '('+str(max_index)+', '+str(len(str1)/2)+')'
#print br[max_index][len(str1)/2]
#print br[len(str2) - max_index][len(str1)/2+1]

if br[len(str2) - max_index][len(str1)/2+1] == 2:
    row = max_index + 1
    col = len(str1)/2 + 1
elif br[len(str2) - max_index][len(str1)/2+1] == 1:
    row = max_index
    col = len(str1)/2 + 1
elif br[len(str2) - max_index][len(str1)/2+1] == 0:
    row = max_index + 1
    col = len(str1)/2

print '('+str(row)+', '+str(col)+')'



##sys.setrecursionlimit(2000)
##
### Backtracking
##def OutputLCS(path1, path2, b, i, j):
###    print i, j, b[i][j]
###     if i == 0 or j == 0:
###         return
##    if i == 0 and j == 0:
##        return
##    if b[i][j] == 0:
##        OutputLCS(path1, path2, b, i-1, j)
##        path1.append(str1[i-1])
##        path2.append('-')
##    elif b[i][j] == 1:
##        OutputLCS(path1, path2, b, i, j-1)
##        path1.append('-')
##        path2.append(str2[j-1])
##    else:
##        OutputLCS(path1, path2, b, i-1, j-1)
##        path1.append(str1[i-1])
##        path2.append(str2[j-1])
##
##path1 = []
##path2 = []
##
##OutputLCS(path1,  path2, b, len(str1), len(str2))
##print ''.join(path1)
##print ''.join(path2)
###print len(path)
