from pypdf import PdfReader

def read_pdf(pdf_name): 
    reader = PdfReader(pdf_name)
    page = reader.pages[0]
    print(page.extract_text("test.pdf"))


def main(): 
    read_pdf("test.pdf")

if __name__ == "__main__": 
    main()