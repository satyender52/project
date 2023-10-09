import PyPDF2

# Paths to the PDF files you want to merge
pdf1_path = r'C:\Users\rozer\Downloads\7d11b02e5abb4717d53b4ce05efabd21.pdf'
pdf2_path = r'C:\Users\rozer\Downloads\da_2023_roadmap.pdf'

# Open both PDF files in binary read mode
with open(pdf1_path, 'rb') as pdf1_file, open(pdf2_path, 'rb') as pdf2_file:
    # Create PDF objects for both files
    pdf1 = PyPDF2.PdfReader(pdf1_file)
    pdf2 = PyPDF2.PdfReader(pdf2_file)

    # Create a PDF writer object to write the merged PDF
    pdf_writer = PyPDF2.PdfWriter()

    # Add pages from the first PDF
    for page in pdf1.pages:
        pdf_writer.add_page(page)

    # Add pages from the second PDF
    for page in pdf2.pages:
        pdf_writer.add_page(page)

    # Path to the output merged PDF file
    merged_pdf_path = r'C:\Users\rozer\Downloads\merged.pdf'

    # Write the merged PDF to a file
    with open(merged_pdf_path, 'wb') as merged_pdf_file:
        pdf_writer.write(merged_pdf_file)

print("PDF files merged successfully to", merged_pdf_path)

