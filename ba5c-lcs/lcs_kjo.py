with open('dataset_74_5.txt','r') as f:
        s = f.readline().strip()
        t = f.readline().strip()

#s = 'AACCTTGG'
#t = 'ACACTGTGA'

import sys
sys.setrecursionlimit(2000)

def outputlcs(b,string,i,j):
	if i == 0 or j == 0:
		return
	if b[i][j] == 0:
		outputlcs(b,string,i-1,j)
	elif b[i][j] == 1:
		outputlcs(b,string,i,j-1)
	else:
		outputlcs(b,string,i-1,j-1)
		#print i,j
		output_list.append(s[j-1])
		

#print len(s)
#print len(t)

matrix = [[0]*(len(s)+1) for i in range(len(t)+1)]
#print matrix

path = [[0]*(len(s)+1) for i in range(len(t)+1)]

for i in range(len(t)):
	for j in range(len(s)):
		matrix[i+1][j+1] = matrix[i][j+1]
		path[i+1][j+1] = 0
		if matrix[i+1][j] > matrix[i+1][j+1]:
			matrix[i+1][j+1] = matrix[i+1][j]
			path[i+1][j+1] = 1
		if t[i] == s[j] and matrix[i][j]+1 > matrix[i+1][j+1]:
			matrix[i+1][j+1] = matrix[i][j]+1
			path[i+1][j+1] = 2

#print matrix
#print path
#print matrix[len(t)][len(s)]

output_list = []
outputlcs(path,s,len(t),len(s))
#print output_list

print ''.join(output_list)
