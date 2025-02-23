# dna_transcription.py

class DnaTranscription:
    """Handles DNA to RNA transcription."""

    def __init__(self, dna_string):
        self.dna_string = dna_string.upper().strip()

    def is_valid_dna(self):
        """Check if the string contains only valid DNA characters."""
        return all(n in "ACGT" for n in self.dna_string)

    def transcribe_dna_to_rna(self):
        """Returns the RNA sequence (replace T with U)."""
        if not self.is_valid_dna():
            return "Error: Invalid DNA sequence."
        return self.dna_string.replace("T", "U")
