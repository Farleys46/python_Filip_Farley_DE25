# Task 1

import matplotlib.pyplot as plt 

# Open the file, and use ".readlines" to read each line and put them in a list

with open("lab1/dna_raw.txt", "r") as file:
    contents = file.readlines()
    

# Creating a dictionary to store the results later. 
dna_counts = {}

#First created a for loop with a jump of 2 at a time then remove the "\n" from the file to clean it.
#Then strip the dna letters aswell as lowercase all letters to be able to count them easily.

for i in range(0, len(contents), 2):
    seq_number = contents[i].strip()
    dna_letters = contents[i + 1].strip().lower()
    
    # This is to count the letters using the ".count" method. The "keys" here are "a,t,c,g" before the colon sign.
    # And the values are what comes after the colon. This is stored in the "counts" dict. 
    
    counts = {
        "a": dna_letters.count("a"),
        "t": dna_letters.count("t"),
        "c": dna_letters.count("c"),
        "g": dna_letters.count("g")
    }

    dna_counts[seq_number] = counts

print("---------- Sequence counts ----------")

# Creating a loop to print the results for each sequence as a dict.
for seq, counts in dna_counts.items():
    print(f"{seq}: {counts}")  

# To create a matplotlib bar graph for every sequence its best to loop it aswell. 
for seq, counts in dna_counts.items():
    plt.figure()
    plt.bar(counts.keys(), counts.values()) # The data that is to be portrayed in the graph. 
    plt.title("DNA letter counts")
    plt.xlabel("letters")
    plt.ylabel("counts")
    plt.show()