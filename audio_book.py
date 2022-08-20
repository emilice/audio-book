import pyttsx3
import PyPDF2

class Reading:
    # path of the PDF file
    file = open('Process Framework.pdf', 'rb')
    
    # creating a PdfFileReader object
    pdfReader = PyPDF2.PdfFileReader(file)
    
    paged=pdfReader.numPages
    print(paged)
    speak = pyttsx3.init()
    # the page with which you want to start
    # this will read the page of 25th page.
    fromPage = pdfReader.getPage(0)
    
    # extracting the text from the PDF
    myText = fromPage.extractText()
    
    # reading the text

    speak.say(myText)
    speak.runAndWait()