import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def classify_diagram(image_path):

    image = Image.open(image_path)

    text = pytesseract.image_to_string(image)

    print("\nOCR Text Found:\n")
    print(text)

    text_upper = text.upper()

    # Biology

    if "PLANT CELL" in text_upper:
        return "Plant Cell"

    if "ANIMAL CELL" in text_upper:
        return "Animal Cell"

    if "HUMAN HEART" in text_upper:
        return "Human Heart"

    if "DIGESTIVE SYSTEM" in text_upper:
        return "Digestive System"

    # Science

    if "WATER CYCLE" in text_upper:
        return "Water Cycle"

    if "SOLAR SYSTEM" in text_upper:
        return "Solar System"

    if "PHOTOSYNTHESIS" in text_upper:
        return "Photosynthesis"

    return "Unknown Educational Diagram"