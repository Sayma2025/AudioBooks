import pyttsx3
from PyPDF2 import PdfReader
book=open('oop pdf.pdf','rb')
pdfReader=PdfReader(book)
pages = len(pdfReader.pages)
print(pages)
# Initialize the pyttsx3 engine
engine = pyttsx3.init()
for num in range(5,pages):
     page = pdfReader.pages[num]  # Accessing page 5 (index 5 corresponds to the 6th page)
     text = page.extract_text()
     engine.say(text)
     engine.runAndWait()
