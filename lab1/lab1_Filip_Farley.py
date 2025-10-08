# Task 1

import matplotlib.pyplot as plt 
# Open the file, and use ".readlines" to read each line and put them in a list
with open("lab1/dna_raw.txt", "r") as file:
    contents = file.readlines()
    

# Creating a dictionary to store the results later. 
dna_counts = {}

#First created a for loop with a jump of 2 at a time then remove the "\n" from the file to clean it.
#Then 
for i in range(0, len(contents), 2):
    seq_number = contents[i].strip()
    dna_letters = contents[i + 1].strip().lower()
    
    counts = {
        "a": dna_letters.count("a"),
        "t": dna_letters.count("t"),
        "c": dna_letters.count("c"),
        "g": dna_letters.count("g")
    }

    dna_counts[seq_number] = counts

for seq, counts in dna_counts.items():
    print(f"{seq}: {counts}")  