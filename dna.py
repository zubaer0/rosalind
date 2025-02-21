#/usr/bin/python3

def count_nucleotides(dna_string):
    # Count occurrences of each nucleotide
    a_count = dna_string.count('A')
    c_count = dna_string.count('C')
    g_count = dna_string.count('G')
    t_count = dna_string.count('T')
    
    # Print the counts separated by spaces
    print(a_count, c_count, g_count, t_count)

# Example usage
dna_string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"  # Example DNA string
count_nucleotides(dna_string)

