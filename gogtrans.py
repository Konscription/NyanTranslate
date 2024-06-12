from googletrans import Translator
import re

def translate_japanese(text_dict,bahasa,asal):
    translator = Translator()
    
     # Removes "[" or "]" characters from each value in the dictionary
    cleaned_text_dict2 = {key: value.replace('［', '').replace('[', '').replace(']', '').replace('「', '').replace('」', '').replace('「', '') for key, value in text_dict.items()}
    cleaned_text_dict = {key: value if value else '・' for key, value in cleaned_text_dict2.items()}
    
    print(cleaned_text_dict)
    
    # Split the text into sentences
    sentences = [value for key, value in cleaned_text_dict.items()]

    # Translate each sentence
    translated_sentences = [translator.translate(sentence, src=asal, dest=bahasa).text for sentence in sentences]

    # Combine the translation results back into the initial form
    translated_text_dict = {key: translated_sentences[i] for i, key in enumerate(cleaned_text_dict.keys())}
    
    hasil_terjemah = {key: value.replace("\'", '’') for key, value in translated_text_dict.items()}

    return hasil_terjemah
