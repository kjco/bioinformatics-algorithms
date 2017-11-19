# peptide practice

peptide = "NQEL"

peptidex2 = peptide + peptide

peptide_len = len(peptide)
peptidex2_len = len(peptidex2)

subpeptides_list = []

for i in range (peptide_len):
    for j in range(peptide_len):
        subpeptides = peptidex2[i:i+j+1]
        subpeptides_list.append(subpeptides)

print subpeptides_list



# for i in range(5):
#    subpeptides = peptide[i-1:i]
#    print subpeptides


# for i in range(5):
#    other = peptide[i-1:i+1]
#    print other


# test = peptide[-1:1]
# print test

# a=3
# letter = peptide[-a]
# print letter


# peptide = peptide + peptide
# print peptide



