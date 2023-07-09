"""
    this module implement translation functions from french to english and from english to french
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
        This function translate text from english to french
    """
    #write the code here
    translator=MyMemoryTranslator(source='en-US', target='fr-FR').translate
    french_text= translator(english_text)
    return french_text

def french_to_english(french_text):
    """
        This function translate text from french to english
    """
    #write the code here
    translator=MyMemoryTranslator(target='en-US', source='fr-FR').translate
    english_text= translator(french_text)
    return english_text
