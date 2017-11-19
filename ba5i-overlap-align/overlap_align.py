import sys

# 0: down, 1: right, 2: lower right

with open('dataset_77_7.txt','r') as f:
    str2 = f.readline().strip()
    str1 = f.readline().strip()

##str2 = 'PAWHEAE'
##str1 = 'HEAGAWGHEE'

# Initialize the matrix
m = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
b = [[0 for j in range(len(str2)+1)] for i in range(len(str1)+1)]
# m = [ [0] * (len(str2)+1) ] * (len(str1)+1)
# b = [ [0] * (len(str2)+1) ] * (len(str1)+1)

#print 'matrix is %dx%d' % (len(m), len(m[0]))

for i in xrange(1, len(str1)+1):
    for j in xrange(1, len(str2)+1):

        m[i][j] = m[i-1][j] - 2
        b[i][j] = 0

        if m[i][j-1] - 2 > m[i][j]:
            m[i][j] = m[i][j-1] - 2
            b[i][j] = 1

        if m[i-1][j-1] - 2 > m[i][j]:
            m[i][j] = m[i-1][j-1] - 2
            b[i][j] = 2

        if str1[i-1] == str2[j-1] and m[i-1][j-1] + 1 > m[i][j]:
            m[i][j] = m[i-1][j-1] + 1
            b[i][j] = 2
            
##        if m[i][j] < 0:
##            m[i][j] = 0
##            b[i][j] = 3

#print m
#print b

max_score = 0

for i in range(len(str1)):
    if m[i][len(str2)] > max_score:
        max_score = m[i][len(str2)]
        v_max = i
##    if m[i][len(str2)] < max_score:
##        break
        
print max_score
#print v_max
#print len(str2)

####max = 0
####predx, predy = 0, 0
####
####for i in xrange(1, len(str1)+1):
####    for j in xrange(1, len(str2)+1):
####        if m[i][j] > max:
####            max = m[i][j]
####            predx, predy = i, j
####
####        #print i,j, m[i][j], b[i][j]
####
#####print b
#####print m[len(str1)][len(str2)]
####print m[predx][predy]


sys.setrecursionlimit(2000)

# Backtracking
# b is list storing path info for backtracking
def OutputLCS(path1, path2, b, i, j):
#   print i, j, b[i][j]
    if i == 0:
        return
#     if i == 0 and j == 0:
#         return
#    if b[i][j] == 3:
#        return
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
OutputLCS(path1,  path2, b, v_max, len(str2))
print ''.join(path2)
print ''.join(path1)
#print len(path)
