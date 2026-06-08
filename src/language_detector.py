def detect_language(text):

    hindi_chars = [
        "अ","आ","इ","ई","उ","ऊ",
        "ए","ऐ","ओ","औ","क","ख",
        "ग","घ","च","छ","ज","झ"
    ]

    for char in hindi_chars:

        if char in text:
            return "Hindi"

    return "English"