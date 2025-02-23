# main.py
import tkinter as tk
from gui import DnaGuiApp

def main():
    root = tk.Tk()
    app = DnaGuiApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
