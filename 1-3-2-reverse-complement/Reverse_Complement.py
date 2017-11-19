# Reverse complement of a sequence

open_seq = open('dataset_3_2.txt','r')
read_seq = open_seq.read()
reverse_seq = read_seq[::-1]

replace_seq = reverse_seq.replace("A","X")
replace_seq = replace_seq.replace("T","A")
replace_seq = replace_seq.replace("C","Z")
replace_seq = replace_seq.replace("G","C")
replace_seq = replace_seq.replace("X","T")
replace_seq = replace_seq.replace("Z","G")

print replace_seq

