# Task 1

#I want to store the data into lists.

seq1 = "cGTAaccaataaaaaaacaagcttaacctaattc"
seq2 = "agcttagTTTGGatctggccgggg"
seq3 = "gcggatttactcCCCCCAAAAANNaggggagagcccagataaatggagtctgtgcgtccaca"
seq4 = "gcggatttactcaggggagagcccagGGataaatggagtctgtgcgtccaca"

a1 = seq1.lower().count("a")
t1 = seq1.lower().count("t")
c1 = seq1.lower().count("c")
g1 = seq1.lower().count("g")
print(f"Sequence 1 has the letter A {a1} times, T {t1} times, C {c1} times and G {g1} times.")