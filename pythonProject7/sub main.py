import PyPDF2

# Replace this with the actual path to your PDF file
pdf_file_path = r'C:\Users\rozer\Downloads\da_2023_roadmap.pdf'

# Open the PDF file in binary read mode
with open(pdf_file_path, 'rb') as pdf_file:
    # Create a PDF object using PdfReader
    pdf = PyPDF2.PdfReader(pdf_file)

    # Get the number of pages in the PDF
    num_pages = len(pdf.pages)

    # Initialize an empty string to store the text
    text = ''

    # Loop through each page and extract text
    for page_num in range(num_pages):
        page = pdf.pages[page_num]
        text += page.extract_text()

# Print the extracted text
print(text)
