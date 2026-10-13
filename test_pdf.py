from pypdf import PdfReader
reader = PdfReader("downloads/latest_saddam_cv.pdf")

print(f"Number of pages: {len(reader.pages)}")

text = reader.pages[0].extract_text()
print(text)