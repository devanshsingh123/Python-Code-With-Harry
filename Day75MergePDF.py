# Write a program to manipulate pdf files using pyPDF. 
# Your programs should be able to merge multiple pdf files into a single pdf.
#  You are welcome to add more functionalities

# pypdf is a free and open-source pure-python PDF library capable of splitting, 
# merging, cropping, and transforming the pages of PDF files.
#  It can also add custom data, viewing options, and passwords to PDF files. pypdf
#  can retrieve text and metadata from PDFs as well.

from pypdf import PdfReader, PdfWriter, PdfMerger
import os
 


readerClassDetails = help(PdfReader)
print(PdfReader.__doc__)




class PDFTools(PdfMerger,PdfReader):
    def __init__(self, pdf_files: list[str]):
        super().__init__()
        self.pdf_files = pdf_files
    
    def read_pdfs(self):
        for pdf in self.pdf_files:
            if os.path.exists(pdf):
                with open(pdf, 'rb') as file:
                    reader = PdfReader(file)
                    print(f"Reading {pdf}: {len(reader.pages)} pages")
            else:
                print(f"File {pdf} does not exist.")

    def merge_pdfs(self, output_file: str):
        for pdf in self.pdf_files:
            self.append(pdf)
        self.write(output_file)
        self.close()
        print(f"Merged {len(self.pdf_files)} PDFs into {output_file}")

    