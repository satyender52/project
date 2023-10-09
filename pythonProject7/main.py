import PyPDF2

# Replace with the path to your PDF file
pdf_file_path =r"C:\Users\rozer\Downloads\7d11b02e5abb4717d53b4ce05efabd21.pdf"

# Open the PDF file in read-binary (rb) mode
with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Check if the PDF file is encrypted
    if pdf_reader.is_encrypted:
        # You may need to provide a password to decrypt it
        password = input("Enter the password for the PDF (if any): ")
        pdf_reader.decrypt(password)

    # Initialize an empty string to store the text
    pdf_text = ""

    # Iterate through each page and extract text
    for page in pdf_reader.pages:
        pdf_text += page.extract_text()

# Print the extracted text
print(pdf_text)




