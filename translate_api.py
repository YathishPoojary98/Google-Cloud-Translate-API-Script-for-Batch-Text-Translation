from google.cloud import translate_v2 as translate
import os
import sys



os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = api_json_file

def translate_text(text, target_language, source_language=None):
    """
    Translates text into the target language.
    
    Args:
        text (str): The text to be translated.
        target_language (str): The language to translate the text into.
        source_language (str, optional): The language of the source text.
        
    Returns:
        str: The translated text.
    """
    # Initialize the Translation client
    client = translate.Client()

    # Perform the translation
    result = client.translate(text, target_language=target_language, source_language=source_language)

    # Return the translated text
    return result['translatedText']

# Example usage
if __name__ == "__main__":
    with open(sys.argv[1],"r") as f:
        data = f.readlines()

    with open(sys.argv[2],"w") as outf:
        for i in range(len(data)):
            text = str(data[i])
            target_language = sys.argv[3]  # Spanish
            translated_text = translate_text(text, target_language)
            outf.write(translated_text)
