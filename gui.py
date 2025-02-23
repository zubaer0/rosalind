# gui.py
import tkinter as tk
from tkinter import filedialog, messagebox
from dna_count import DnaCount
from dna_transcription import DnaTranscription
from reverse_complement import ReverseComplement

class DnaGuiApp:
    """GUI for DNA Analysis: Nucleotide Counting, Transcription, and Reverse Complement."""

    def __init__(self, root):
        self.root = root
        self.root.title("DNA Analyzer")
        self.root.geometry("400x350")

        # Label
        tk.Label(root, text="Enter DNA String or Upload File:").pack()

        # Entry Field
        self.entry = tk.Entry(root, width=50)
        self.entry.pack()

        # Buttons
        tk.Button(root, text="Count Nucleotides", command=self.process_counting).pack(pady=5)
        tk.Button(root, text="Transcribe DNA to RNA", command=self.process_transcription).pack(pady=5)
        tk.Button(root, text="Reverse Complement", command=self.process_reverse_complement).pack(pady=5)
        tk.Button(root, text="Upload File", command=self.process_file_input).pack(pady=5)

        # Result Label
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def get_dna_string(self):
        """Get the DNA sequence from the entry box."""
        return self.entry.get().strip()

    def process_counting(self):
        """Process nucleotide counting."""
        dna_string = self.get_dna_string()
        processor = DnaCount(dna_string)
        result = processor.count_nucleotides()

        if isinstance(result, dict):
            result_text = f"A: {result['A']}, C: {result['C']}, G: {result['G']}, T: {result['T']}"
        else:
            result_text = result  # Error message

        self.result_label.config(text=result_text)

    def process_transcription(self):
        """Process DNA transcription."""
        dna_string = self.get_dna_string()
        processor = DnaTranscription(dna_string)
        result = processor.transcribe_dna_to_rna()
        self.result_label.config(text=result)

    def process_reverse_complement(self):
        """Process Reverse Complement of DNA."""
        dna_string = self.get_dna_string()
        processor = ReverseComplement(dna_string)
        result = processor.reverse_complement()
        self.result_label.config(text=result)

    def process_file_input(self):
        """Handles file input and reads DNA sequence from a file."""
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    dna_string = file.read().strip()
                self.entry.delete(0, tk.END)
                self.entry.insert(0, dna_string)
            except Exception as e:
                messagebox.showerror("File Error", f"Could not read file: {e}")
