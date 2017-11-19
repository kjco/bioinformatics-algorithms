# peptides

#peptide = "IAQMLFYCKVATN"
open_file = open('dataset_20_3.txt', 'r')
peptide = open_file.readline().rstrip('\n')
open_file.close()

peptidex2 = peptide + peptide

peptide_len = len(peptide)
peptidex2_len = len(peptidex2)

subpeptides_list = []

for i in range (peptide_len):
    for j in range(peptide_len-1):
        subpeptides = peptidex2[i:i+j+1]
        subpeptides_list.append(subpeptides)

# The above for loop does not include the full length peptide fragment
# May need to append as extra

subpeptides_list.append(peptide)

#subpeptides_list_nr = []
#subpeptides_list_nr = list(set(subpeptides_list))
#print subpeptides_list_nr
subpeptides_list_nr = subpeptides_list

subpeptides_list_nr_len = len(subpeptides_list_nr)

subpeptides_size = []
peptide_mass = 0
mass_dict = {'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}

for n in range(subpeptides_list_nr_len):
    list_items = subpeptides_list_nr[n]
    list_items_len = len(list_items)
    peptide_mass = 0
    for m in range(list_items_len):
        character = list_items[m]
        peptide_mass = peptide_mass+ mass_dict[character]
    if peptide_mass == 71:
        print list_items
    subpeptides_size.append(peptide_mass)

subpeptides_size_sort = sorted(subpeptides_size)
#print subpeptides_size_sort

results = map(str, subpeptides_size_sort)
print results

print ' '.join(results)

