# finding the composition of a string text

with open('dataset_51_3.txt','r') as f:
    k = int(f.readline().rstrip('\n'))
    text = f.readline().rstrip('\n')
#k =5
#text = 'CAATCCAAC'
comp_list = []

#print k
#print text
#print len(text)

for i in range(len(text)-k+1):
    comp = text[i:i+k]
    comp_list.append(comp)

lex_comp_list = sorted(comp_list)

#print comp_list
#print lex_comp_list
print '\n'.join(lex_comp_list)

