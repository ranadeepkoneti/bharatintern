#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install googletrans==4.0.-rc1


# In[2]:


from googletrans import Translator

def translate_text(text, src_lang='auto', dest_lang='en'):
    """
    Translate text from the source language to the destination language.

    Parameters:
        text (str): The input text to be translated.
        src_lang (str): The source language code (e.g., 'en' for English, 'fr' for French).
                        Set 'auto' to let Google Translate detect the source language.
        dest_lang (str): The destination language code (e.g., 'en' for English, 'fr' for French).

    Returns:
        str: The translated text in the destination language.
    """
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text
    return translated_text

# Example usage:
input_text = "Hello, how are you?"
target_language = "fr"  # French

translated_text = translate_text(input_text, dest_lang=target_language)

# Display the results
print(f"Original text: {input_text}")
print(f"Translated text: {translated_text}")


# In[ ]:




