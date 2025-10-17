# Task 2

import matplotlib.pyplot as plt 

# Open the file, and use ".readlines" to read each line and put them in a list

def data_file(filename):
    
    # Creating a dictionary to store the results later. 
    dna_counts = {}
    seq_number = None # Keeps track of which sequence your on. When line starts with ">" its a new seq.  
    dna_letters = [] # To store the value in each key, (dna letters)
    
    with open(filename, "r") as file:
        for raw_line in file:
            line = raw_line.strip()
            
            if line.startswith(">"): # Checks if line starts with a ">" to determine what is value and what is key.
                if seq_number is not None:
                    full_seq = "".join(dna_letters).lower() # Join the dna letters together in a single string. And lower the them for easier counting. 
                    
                    # Counting the "a", "t", "c", "g"
                    dna_counts[seq_number] = {
                        "a": full_seq.count("a"),
                        "t": full_seq.count("t"),
                        "c": full_seq.count("c"),
                        "g": full_seq.count("g")
                    }
                
                seq_number = line
                dna_letters = []
            
            else:
                dna_letters.append(line)
        
        if seq_number is not None:
            full_seq = "".join(dna_letters).lower()
            dna_counts[seq_number] = {
                        "a": full_seq.count("a"),
                        "t": full_seq.count("t"),
                        "c": full_seq.count("c"),
                        "g": full_seq.count("g")
                    }


# Got inspiration from classmates to make it look nicer. 
    print("------------ Sequence counts ------------")

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

# Calling for the function "data_file" i created and putting in which file i want to use. 
data_file("C:/Users/filip/OneDrive/Desktop/DE25/python_Filip_Farley_DE25/lab1/dna_raw_complicated.txt")