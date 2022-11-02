import openpyxl
from fpdf import FPDF
import fitz

with fitz.open("students.pdf") as pdf:
    # The fitz open object is a list of pages, so we can access each at once iterably
    for page in pdf:
        print(page.get_text())