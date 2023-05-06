import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileFormatAnalyzerGUI:
    def __init__(self, master):
        self.master = master
        master.title("File Format Analyzer")

        # Create a menu bar with an option to select the drive to analyze
        self.menu_bar = tk.Menu(master)
        self.master.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Select drive", command=self.select_drive)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Create a frame to hold the results section
        self.results_frame = tk.Frame(master)
        self.results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Create a listbox to display the file format results
        self.file_format_label = tk.Label(self.results_frame, text="File Formats", font=("Arial", 14))
        self.file_format_label.pack(pady=(0,10))
        self.file_format_listbox = tk.Listbox(self.results_frame, height=10, width=50)
        self.file_format_listbox.pack()

        # Create a separator
        self.separator = tk.Frame(self.results_frame, height=2, bd=1, relief=tk.SUNKEN)
        self.separator.pack(fill=tk.X, pady=(20,10))

        # Create a label and listbox to display the hidden file results
        self.hidden_file_label = tk.Label(self.results_frame, text="Hidden Files", font=("Arial", 14))
        self.hidden_file_label.pack(pady=(10,5))
        self.hidden_file_listbox = tk.Listbox(self.results_frame, height=3, width=50)
        self.hidden_file_listbox.pack()

        # Create a label and listbox to display the non-hidden file results
        self.non_hidden_file_label = tk.Label(self.results_frame, text="Non-Hidden Files", font=("Arial", 14))
        self.non_hidden_file_label.pack(pady=(10,5))
        self.non_hidden_file_listbox = tk.Listbox(self.results_frame, height=3, width=50)
        self.non_hidden_file_listbox.pack()

    def select_drive(self):
        # Get the drive letter from the user and validate it
        drive_letter = filedialog.askdirectory()
        if not os.path.exists(drive_letter):
            messagebox.showerror("Error", "Drive path does not exist.")
            return

        # Analyze the files in the drive and display the results in the listbox
        self.file_format_listbox.delete(0, tk.END)
        self.hidden_file_listbox.delete(0, tk.END)
        self.non_hidden_file_listbox.delete(0, tk.END)

        file_formats = {}
        hidden_file_size = 0
        non_hidden_file_size = 0
        for root, dirs, files in os.walk(drive_letter):
            for file in files:
                file_path = os.path.join(root, file)
                file_format = os.path.splitext(file_path)[1]
                if file_format in file_formats:
                    file_formats[file_format] += 1
                else:
                    file_formats[file_format] = 1
                if os.path.isfile(file_path):
                    file_size = os.path.getsize(file_path)
                    if file_path.startswith('.'):
                        hidden_file_size += file_size
                    else:
                        non_hidden_file_size += file_size

        for file_format, count in file_formats.items():
            self.file_format_listbox.insert(tk.END, f"{file_format}: {count}")

        self.hidden_file
