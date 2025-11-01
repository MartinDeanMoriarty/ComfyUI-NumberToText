from typing import Any
from num2words import num2words

class NumberToTextNode:
    # Converts a number (e.g., 2) into written text (e.g., 'two').
    # Uses the 'num2words' library for multilingual support.    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "number": ("STRING", {"default": "2", "multiline": False}),
                "language": (["de", "en"], {"default": "de"}),  # Deutsch or English
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "convert"
    CATEGORY = "DeanLogic"

    def convert(self, number: str, language: str) -> tuple[str]:
        # Try, to convert to number
        try:
            num = int(number)
        except ValueError:
            try:
                num = float(number)
            except ValueError:
                return (number,)  # Not a number, just return

        # Use num2words for better translation
        try:
            if language == "en":
                text = num2words(num, lang='en')
            elif language == "de":
                text = num2words(num, lang='de')
            else:
                text = str(num)  # If language is not supported
        except ValueError:
            text = str(num)  # Error, if the number does not parse

        return (text,)
