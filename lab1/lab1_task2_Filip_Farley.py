# Task 2

import matplotlib.pyplot as plt 

# Open the file, and use ".readlines" to read each line and put them in a list

def data_file(filename):
    
    # Creating a dictionary to store the results later. 
    dna_counts = {}
    seq_number = None
    dna_letters = []
    
    with open(filename, "r") as file:
        contents = file.readlines()
        for raw_line in file:
            line = raw_line.strip()
            if line == "":
                continue
            
            if line.startswith(">"):
                if seq_number is not None:
                    full_seq = "".join(dna_letters).lower()
                    
                    
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
    print("---------- Sequence counts ----------")

# Creating a loop to print the results for each sequence as a dict.
    for seq, counts in dna_counts.items():
        print(f"{seq}: {dna_counts}")  

# To create a matplotlib bar graph for every sequence its best to loop it aswell. 
    for seq, counts in dna_counts.items():
        plt.figure()
        plt.bar(counts.keys(), counts.values()) # The data that is to be portrayed in the graph. 
        plt.title("DNA letter counts")
        plt.xlabel("letters")
        plt.ylabel("counts")
        plt.show()

data_file("C:/Users/filip/OneDrive/Desktop/DE25/python_Filip_Farley_DE25/Testing/dna_raw.txt")