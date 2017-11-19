import sys

# 0: down, 1: right, 2: lower right
sigma = 5

# Read the scoring matrix
d = dict()
with open('PAM250_1.txt') as f:
    alphabets = f.readline().strip().split()

    for line in f:
        chars = line.strip().split()
        m = chars[0]
        scores = map(int, chars[1:])
        for i in range(len(scores)):
            d[(m, alphabets[i])] = scores[i]

#print d

#with open('data.txt') as f:
with open('dataset_76_9.txt') as f:
    str1 = f.readline().strip()
    str2 = f.readline().strip()

# Initialize the matrix
m = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
b = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
# m = [ [0] * (len(str2)+1) ] * (len(str1)+1)
# b = [ [0] * (len(str2)+1) ] * (len(str1)+1)

print 'matrix is %dx%d' % (len(m), len(m[0]))

for i in xrange(1, len(str1)+1):
    for j in xrange(1, len(str2)+1):

#         if m[i-1][j] - sigma > m[i][j]:
#             m[i][j] = m[i-1][j] - sigma
#             b[i][j] = 0
        m[i][j] = m[i-1][j] - sigma
        b[i][j] = 0

        if m[i][j-1] - sigma > m[i][j]:
            m[i][j] = m[i][j-1] - sigma
            b[i][j] = 1

        score =  m[i-1][j-1] + d[(str1[i-1], str2[j-1])]
        # print str1[i-1], str2[j-1], d[(str1[i-1], str2[j-1])]
        if score > m[i][j]:
            m[i][j] = score
            b[i][j] = 2
            
        if m[i][j] < 0:
            m[i][j] = 0
            b[i][j] = 3


max = 0
predx, predy = 0, 0

for i in xrange(1, len(str1)+1):
    for j in xrange(1, len(str2)+1):
        if m[i][j] > max:
            max = m[i][j]
            predx, predy = i, j

        #print i,j, m[i][j], b[i][j]

#print b
#print m[len(str1)][len(str2)]
print m[predx][predy]


sys.setrecursionlimit(2000)

# Backtracking
# b is list storing path info for backtracking
def OutputLCS(path1, path2, b, i, j):
#   print i, j, b[i][j]
    if i == 0 or j == 0:
        return
#     if i == 0 and j == 0:
#         return
    if b[i][j] == 3:
        return
    elif b[i][j] == 0:
        OutputLCS(path1, path2, b, i-1, j)
        path1.append(str1[i-1])
        path2.append('-')
    elif b[i][j] == 1:
        OutputLCS(path1, path2, b, i, j-1)
        path1.append('-')
        path2.append(str2[j-1])
    else:
        OutputLCS(path1, path2, b, i-1, j-1)
        path1.append(str1[i-1])
        path2.append(str2[j-1])

path1 = []
path2 = []

#OutputLCS(path1,  path2, b, len(str1), len(str2))
OutputLCS(path1,  path2, b, predx, predy)
print ''.join(path1)
print ''.join(path2)
#print len(path)
