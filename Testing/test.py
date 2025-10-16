cleaned_lines = []
current_id = None
sequence_parts = []

with open("C:/Users/filip/OneDrive/Desktop/DE25/python_Filip_Farley_DE25/Testing/dna_raw_complicated.txt", "r") as file_r:
    for line in file_r:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if current_id:
                cleaned_lines.append(current_id)
                cleaned_lines.append("".join(sequence_parts))
            current_id = line
            sequence_parts = []
        else:
            sequence_parts.append(line)
if current_id:
    cleaned_lines.append(current_id)
    cleaned_lines.append("".join(sequence_parts))

with open("...dna_raw_complicated_cleaned.txt", "w") as file_w:
    for line in cleaned_lines:
        file_w.write(line + "\n")
