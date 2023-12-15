from pytesseract import pytesseract

class OCR:
    def __init__(self):
        self.path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        pytesseract.tesseract_cmd = self.path

    def extract(self, filename, language='eng'):
        try:
            # Specify the language using the lang parameter
            text = pytesseract.image_to_string(filename, lang=language)
            return text
        except Exception as e:
            print(e)
            return "Error"

# Create an instance of the OCR class
ocr = OCR()

# Specify the language code for Tamil (tam)
tamil_language_code = 'tam'

# Call the extract method with the filename and language parameter
text = ocr.extract("tamil.jpg", language=tamil_language_code)

# Print the extracted text
print(text)
