import sys

# 0: down, 1: right, 2: lower right

with open('dataset_74_5.txt') as f:
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
        m[i][j] = m[i-1][j]
        b[i][j] = 0

        if m[i][j-1] > m[i][j]:
            m[i][j] = m[i][j-1]
            b[i][j] = 1

        if str1[i-1] == str2[j-1] and m[i-1][j-1] + 1 > m[i][j]:
            m[i][j] = m[i-1][j-1] + 1
            b[i][j] = 2

        #print i,j, m[i][j], b[i][j]

#print b
print m[len(str1)][len(str2)]


sys.setrecursionlimit(2000)

# Backtracking
def OutputLCS(path, b, str, i, j):
#    print i, j, b[i][j]
    if i == 0 or j == 0:
        return
    if b[i][j] == 0:
        OutputLCS(path, b, str, i-1, j)
    elif b[i][j] == 1:
        OutputLCS(path, b, str, i, j-1)
    else:
        OutputLCS(path, b, str, i-1, j-1)
        path.append(str[i-1])

path = []

OutputLCS(path, b, str1, len(str1), len(str2))
print ''.join(path)
#print len(path)
