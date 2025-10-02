import matplotlib.pyplot as plt

sequences = {
    "Sequence 1": "cGTAaccaataaaaaaacaagcttaacctaattc",
    "Sequence 2": "agcttagTTTGGatctggccgggg",
    "Sequence 3": "gcggatttactcCCCCCAAAAANNaggggagagcccagataaatggagtctgtgcgtccaca",
    "Sequence 4": "gcggatttactcaggggagagcccagGGataaatggagtctgtgcgtccaca"
}

for name, seq in sequences.items():
    seq = seq.lower()
    counts = {
        "A": seq.count("a"),
        "T": seq.count("t"),
        "C": seq.count("c"),
        "G": seq.count("g")
    }

    plt.bar(counts.keys(), counts.values())
    plt.title(f"DNA Letter Frequency - {name}")
    plt.xlabel("DNA Letter")
    plt.ylabel("Count")
    plt.show()
