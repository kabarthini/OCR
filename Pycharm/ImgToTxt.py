from pytesseract import pytesseract

class OCR:
    def __init__(self, tesseract_path, languages=None):
        self.path = tesseract_path
        pytesseract.tesseract_cmd = self.path
        self.languages = languages or []

    def extract(self, filename):
        try:
            # Concatenate language codes into a single string, separated by '+'
            lang_str = '+'.join(self.languages)
            # Specify multiple languages using the lang parameter as a single string
            text = pytesseract.image_to_string(filename, lang=lang_str, config='--psm 6 --oem 3')
            return text
        except Exception as e:
            print(e)
            return "Error"

# Create an instance of the OCR class with both English and Hindi languages
tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
languages_to_extract = ['eng']
ocr = OCR(tesseract_path, languages=languages_to_extract)

# Call the extract method with the filename
text = ocr.extract("DL.jpg")

# Print the extracted text
print(text)


