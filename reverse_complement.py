# reverse_complement.py

class ReverseComplement:
    """Handles reverse complement of a DNA string."""

    def __init__(self, dna_string):
        self.dna_string = dna_string.upper().strip()

    def is_valid_dna(self):
        """Check if the string contains only valid DNA characters."""
        return all(n in "ACGT" for n in self.dna_string)

    def reverse_complement(self):
        """Returns the reverse complement of the DNA sequence."""
        if not self.is_valid_dna():
            return "Error: Invalid DNA sequence."

        complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
        return "".join(complement[base] for base in reversed(self.dna_string))
