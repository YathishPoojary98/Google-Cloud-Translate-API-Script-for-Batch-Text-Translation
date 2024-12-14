## Google Cloud Translate API Script for Batch Text Translation

Key Features:

Batch Translation: Translates multiple lines of text from a file.

Language Support: Supports all languages available in the Google Cloud Translation API.

Easy Configuration: Set your credentials, input file, output file, and target language via command-line arguments.

Usage:

python translate_script.py input.txt output.txt target_language

input.txt: File containing the text to be translated.

output.txt: File to save the translated text.

target_language: Language code for the target language (e.g., es for Spanish, fr for French).

Prerequisites:

Google Cloud account with the Translation API enabled.
Service account key (JSON) for authentication.
google-cloud-translate library installed.

Example:

python translate_script.py data.txt translated_data.txt es

This translates the content of data.txt into Spanish and writes the output to translated_data.txt.
