import tkinter as tk
from tkinter import ttk, filedialog
import re
import time

# Placeholder function for extracting text from a PDF (using pdfminer)
from pdfminer.high_level import extract_text

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_name_from_resume(text):
    name = None
    # Use regex pattern to find a potential name
    pattern = r"([A-Z][a-z]+(?: [A-Z][a-z]+)+)"
    match = re.search(pattern, text)
    if match:
        name = match.group()
    return name

def extract_contact_number_from_resume(text):
    contact_number = None
    # Use regex pattern to find a potential contact number
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    if match:
        contact_number = match.group()
    return contact_number

def extract_email_from_resume(text):
    email = None
    # Use regex pattern to find a potential email address
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, text)
    if match:
        email = match.group()
    return email

def extract_skills_from_resume(text):
    skills = []
    # List of skills (you can modify this as needed)
    skills_list = ['C', 'C++', 'Java', 'HTML', 'CSS', 'JavaScript', 'Python', 'MySQL', 'MongoDB', 'Data Analysis', 'Machine Learning', 'Communication', 'Project Management', 'Deep Learning', 'SQL', 'Tableau']
    for skill in skills_list:
        pattern = r"\b{}\b".format(re.escape(skill))
        if re.search(pattern, text, re.IGNORECASE):
            skills.append(skill)
    return skills

def extract_education_from_resume(text):
    education = []
    # Use regex pattern to find education information
    pattern = r"(?i)(?:Bsc|\bB\.\w+|\bM\.\w+|\bPh\.D\.\w+|\bBachelor of Technology Computer Science and Engineering(?:'s)?|\bMaster(?:'s)?|\bPh\.D)\s(?:\w+\s)*\w+"
    matches = re.findall(pattern, text)
    for match in matches:
        education.append(match.strip())
    return education

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        # Extract information from the resume
        text = extract_text_from_pdf(file_path)
        name = extract_name_from_resume(text)
        contact_number = extract_contact_number_from_resume(text)
        email = extract_email_from_resume(text)
        skills = extract_skills_from_resume(text)
        education = extract_education_from_resume(text)

        # Display the extracted information in the GUI
        name_entry.delete(0, tk.END)
        contact_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        skills_entry.delete(0, tk.END)
        education_entry.delete(0, tk.END)

        name_entry.insert(0, name if name else "Name not found")
        contact_entry.insert(0, contact_number if contact_number else "Contact Number not found")
        email_entry.insert(0, email if email else "Email not found")
        skills_entry.insert(0, ", ".join(skills) if skills else "No skills found")
        education_entry.insert(0, ", ".join(education) if education else "No education found")

def animate_title(text, widget, duration=0.02):
    widget.config(text="")
    for char in text:
        widget.config(text=widget.cget("text") + char)
        widget.update()
        time.sleep(duration)

# Create the main window
root = tk.Tk()
root.title("Resume Parser")
root.geometry("800x600")

# Define styles
title_style = ("Arial", 24, "bold")
label_style = ("Arial", 14)
entry_style = ("Arial", 12)

# Create and place labels and entry fields
title_label = ttk.Label(root, font=title_style)
title_label.pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=10)

browse_btn = tk.Button(frame, text="Browse PDF", command=browse_file, font=entry_style)
browse_btn.pack(side=tk.LEFT, padx=10)

name_label = tk.Label(root, text="Name:", font=label_style)
name_label.pack(anchor="w", padx=20)

name_entry = tk.Entry(root, width=50, font=entry_style)
name_entry.pack()

contact_label = tk.Label(root, text="Contact Number:", font=label_style)
contact_label.pack(anchor="w", padx=20)

contact_entry = tk.Entry(root, width=50, font=entry_style)
contact_entry.pack()

email_label = tk.Label(root, text="Email:", font=label_style)
email_label.pack(anchor="w", padx=20)

email_entry = tk.Entry(root, width=50, font=entry_style)
email_entry.pack()

skills_label = tk.Label(root, text="Skills:", font=label_style)
skills_label.pack(anchor="w", padx=20)

skills_entry = tk.Entry(root, width=50, font=entry_style)
skills_entry.pack()

education_label = tk.Label(root, text="Education:", font=label_style)
education_label.pack(anchor="w", padx=20)

education_entry = tk.Entry(root, width=50, font=entry_style)
education_entry.pack()

# Animate the title
animate_title("Resume Parser", title_label)

root.mainloop()
