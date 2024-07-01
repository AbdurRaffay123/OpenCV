import PyPDF2

def compare_pdfs(file1, file2):
    # Open the PDF files
    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        pdf1 = PyPDF2.PdfReader(f1)
        pdf2 = PyPDF2.PdfReader(f2)
        
        # Check if the number of pages is the same
        if len(pdf1.pages) != len(pdf2.pages):
            return False
        
        # Compare text content page by page
        for i in range(len(pdf1.pages)):
            page1_text = pdf1.pages[i].extract_text()
            page2_text = pdf2.pages[i].extract_text()
            
            if page1_text != page2_text:
                return False
            
    return True

if __name__ == '__main__':
    file1 = "Pdf/A1.pdf"
    file2 = "Pdf/A1.pdf"
    
    if compare_pdfs(file1, file2):
        print("PDFs are identical")
    else:
        print("PDFs are not identical")