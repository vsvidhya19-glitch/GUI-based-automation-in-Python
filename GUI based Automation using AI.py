import os
import pandas as pd
import tkinter as tk

from tkinter import filedialog, messagebox

def clean_data():
    input_file = input_path.get()
    output_folder = output_path.get()

    if not input_file or not output_folder:
        messagebox.showerror("Error", "Please select both input file and output folder.")
        return

    try:
        df = pd.read_excel(input_file)

        # Apply cleaning options dynamically
        if remove_duplicates.get():
            df = df.drop_duplicates()

        if remove_blank.get():
            df = df.dropna(how="all")

        if strip_spaces.get():
            for col in df.select_dtypes(include="object").columns:
                df[col] = df[col].str.strip()

        if title_case.get():
            for col in df.select_dtypes(include="object").columns:
                df[col] = df[col].str.title()

        # Save cleaned file
        output_file = os.path.join(output_folder, "Cleaned_Data.xlsx")
        df.to_excel(output_file, index=False)
        messagebox.showinfo("Success", f"Cleaned file saved at:\n{output_file}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

def browse_input():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    input_path.set(file_path)

def browse_output():
    folder_path = filedialog.askdirectory()
    output_path.set(folder_path)

def reset_paths():
    input_path.set("")
    output_path.set("")

def reset_checkboxes():
    remove_duplicates.set(False)
    remove_blank.set(False)
    strip_spaces.set(False)
    title_case.set(False)

# GUI Setup
root = tk.Tk()
root.title("Dynamic Data Cleaning Automation")

input_path = tk.StringVar()
output_path = tk.StringVar()

remove_duplicates = tk.BooleanVar()
remove_blank = tk.BooleanVar()
strip_spaces = tk.BooleanVar()
title_case = tk.BooleanVar()

# Input file selection
tk.Label(root, text="Select Input Excel File:").grid(row=0, column=0, sticky="w")
tk.Entry(root, textvariable=input_path, width=50).grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_input).grid(row=0, column=2)

# Output folder selection
tk.Label(root, text="Select Output Folder:").grid(row=1, column=0, sticky="w")
tk.Entry(root, textvariable=output_path, width=50).grid(row=1, column=1)
tk.Button(root, text="Browse", command=browse_output).grid(row=1, column=2)

# Cleaning options
tk.Label(root, text="Data Cleaning Options:").grid(row=2, column=0, sticky="w")
tk.Checkbutton(root, text="Remove Duplicate Rows", variable=remove_duplicates).grid(row=3, column=0, sticky="w")
tk.Checkbutton(root, text="Remove Blank Rows", variable=remove_blank).grid(row=4, column=0, sticky="w")
tk.Checkbutton(root, text="Trim Spaces in Text Columns", variable=strip_spaces).grid(row=5, column=0, sticky="w")
tk.Checkbutton(root, text="Title Case Text Columns", variable=title_case).grid(row=6, column=0, sticky="w")

# Buttons
tk.Button(root, text="Clean Data", command=clean_data, bg="lightgreen").grid(row=7, column=0, pady=10)
tk.Button(root, text="Reset Paths", command=reset_paths, bg="lightblue").grid(row=7, column=1, pady=10)
tk.Button(root, text="Reset Checkboxes", command=reset_checkboxes, bg="lightyellow").grid(row=7, column=2, pady=10)

root.mainloop()