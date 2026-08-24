from __future__ import annotations

import tempfile
from pathlib import Path
from typing import Optional

from pypdf import PdfReader
import docx2txt


def read_uploaded_file(uploaded_file) -> str:
    """Read txt, pdf, or docx uploaded from Streamlit."""
    if uploaded_file is None:
        return ""

    suffix = Path(uploaded_file.name).suffix.lower()

    if suffix == ".txt":
        return uploaded_file.read().decode("utf-8", errors="ignore") #read will read bytes and decode convert it in to python text


    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.getvalue())#loads data and writes it in temporary file
        tmp_path = tmp.name


#                      Create temporary file

# For PDF and DOCX files:

# with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:

# This creates a temporary file.

# For example:

# Uploaded resume.pdf
#         ↓
# Temporary file
#         ↓
# C:\Users\...\Temp\tmpabc123.pdf
    if suffix == ".pdf":
        reader = PdfReader(tmp_path)
        text = []
        for page in reader.pages:
            text.append(page.extract_text() or "")
        return "\n".join(text)

    if suffix == ".docx":
        return docx2txt.process(tmp_path)

    raise ValueError("Unsupported file type. Please upload .txt, .pdf, or .docx")




#     10. PDF processing
# if suffix == ".pdf":

# If the uploaded file is a PDF, this block executes.

# reader = PdfReader(tmp_path)

# PdfReader opens the PDF.

# For example:

# resume.pdf
#    ↓
# PdfReader
#    ↓
# PDF pages
# 11. Create empty list
# text = []

# This will store the text extracted from each PDF page.

# Suppose the PDF has 3 pages:

# Page 1 → text[0]
# Page 2 → text[1]
# Page 3 → text[2]
# 12. Loop through pages
# for page in reader.pages:

# This processes every page of the PDF.

# For example:

# PDF
# │
# ├── Page 1
# ├── Page 2
# ├── Page 3
# └── Page 4

# The loop visits each page.

# 13. Extract text
# text.append(page.extract_text() or "")

# This is an important line.

# page.extract_text()

# attempts to extract text from the current page.

# If successful:

# Python
# React
# Machine Learning
# AWS

# gets added to the text list.

# If there is no extractable text, this:

# or ""

# ensures that an empty string is added instead of None.

# 14. Combine PDF pages
# return "\n".join(text)

# Suppose:

# text = [
#     "Name: Dinesh\nPython\nReact",
#     "Skills: SQL\nAWS",
#     "Experience: 2 years"
# ]

# Then:

# "\n".join(text)

# produces:

# Name: Dinesh
# Python
# React
# Skills: SQL
# AWS
# Experience: 2 years

# Now the complete PDF has been converted into plain text.

# 15. DOCX processing
# if suffix == ".docx":
#     return docx2txt.process(tmp_path)

# If the uploaded file is:

# resume.docx

# the program sends the temporary file to:

# docx2txt.process()

# which extracts the text.

# For example:

# resume.docx
#      ↓
# docx2txt
#      ↓
# "Python Developer with experience in..."
# 16. Unsupported files

# Finally:

# raise ValueError(
#     "Unsupported file type. Please upload .txt, .pdf, or .docx"
# )

# Suppose someone uploads:

# resume.jpg

# or:
