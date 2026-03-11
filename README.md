# GUI-based-automation-in-Python
This repository contains a Python-based GUI application built with Tkinter that automates common data-cleaning tasks for Excel files. It provides a user-friendly interface to select input files, choose cleaning operations, and export cleaned data with just a few clicks.
✨ Features
- Browse Input File: Select any raw Excel file.
- Browse Output Folder: Choose where the cleaned file will be saved.
- Data Cleaning Options (via checkboxes):
- Remove duplicate rows
- Remove blank rows
- Trim leading/trailing spaces in text columns
- Convert text columns to Title Case
- Buttons:
- Clean Data → Apply selected cleaning operations and export the file.
- Reset Paths → Clear input/output selections.
- Reset Checkboxes → Uncheck all cleaning options.
⚡ How It Works
- Launch the GUI.
- Browse and select an Excel file.
- Choose one or more cleaning options.
- Select an output folder.
- Click Clean Data to generate a cleaned Excel file automatically saved in the chosen folder.
🛠️ Tech Stack
- Python 3.x
- Tkinter (GUI framework)
- Pandas (data manipulation)
- Openpyxl / XlsxWriter (Excel file handling)
📂 Output
The cleaned file is saved as Cleaned_Data.xlsx in the selected output folder.



