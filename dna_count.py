# dna_count.py

class DnaCount:
    """Handles nucleotide counting in a DNA string."""

    def __init__(self, dna_string):
        self.dna_string = dna_string.upper().strip()

    def is_valid_dna(self):
        """Check if the string contains only valid DNA characters."""
        return all(n in "ACGT" for n in self.dna_string)

    def count_nucleotides(self):
        """Returns a dictionary with counts of A, C, G, and T."""
        if not self.is_valid_dna():
            return "Error: Invalid DNA sequence (must contain only A, C, G, and T)."

        return {
            "A": self.dna_string.count("A"),
            "C": self.dna_string.count("C"),
            "G": self.dna_string.count("G"),
            "T": self.dna_string.count("T"),
        }
