
down_list = [ map(int,line.split()) for line in open('dataset_72_9.txt','r')]
right_list = [ map(int,line.split()) for line in open('dataset_72_9_2.txt','r')]

#down_list = [[1,0,2,4,3],[4,6,5,2,1],[4,4,5,2,1],[5,6,8,5,3]]
#right_list = [[3,2,4,0],[3,2,4,2],[0,7,3,3],[3,3,0,2],[1,3,2,2]]

n = 8
m = 10

matrix = [[0]*(m+1) for i in range(n+1)]

for i in range(4):
    matrix[0][i+1] = right_list[0][i]
    matrix[i+1][0] = down_list[i][0]

#print matrix

##for i in range(4):
##    if matrix[i][i+1] + down_list[i][i+1] > matrix[i+1][i] + right_list[i+1][i]:
##        matrix[i+1][i+1] = matrix[i][i+1] + down_list[i][i+1]
##    else:
##        matrix[i+1][i+1] = matrix[i+1][i] + right_list[i+1][i]
##
##print matrix


for i in range(n):
    for j in range(m):
        if matrix[i][j+1] + down_list[i][j+1] > matrix[i+1][j] + right_list[i+1][j]:
            matrix[i+1][j+1] = matrix[i][j+1] + down_list[i][j+1]
        else:
            matrix[i+1][j+1] = matrix[i+1][j] + right_list[i+1][j]

#print matrix
print matrix[n][m]
