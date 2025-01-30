# 🌍 Google Cloud Translate API Script for Batch Text Translation

A Python script for **batch text translation** using the **Google Cloud Translation API**, allowing seamless multilingual text processing. This tool is ideal for automating text translation workflows by processing multiple lines from an input file efficiently.

---

## 🚀 Key Features

✅ **Batch Translation** – Translates multiple lines of text from a file.  
✅ **Language Support** – Supports all languages available in the **Google Cloud Translation API**.  
✅ **Easy Configuration** – Set **credentials, input file, output file, and target language** via command-line arguments.  

---

## 🛠 Prerequisites

Before using the script, ensure you have the following:

1️⃣ **Google Cloud Account**  
   - Enable the **Cloud Translation API** in your Google Cloud account.  

2️⃣ **Service Account Key (JSON)**  
   - Download your **service account key** for authentication.  

3️⃣ **Install Required Libraries**  
   Install the `google-cloud-translate` library using:
   ```bash
   pip install google-cloud-translate
```
📌 Usage
Run the script using the following command:

```bash
python translate_script.py input.txt output.txt target_language
```
Arguments:
input.txt – File containing the text to be translated.
output.txt – File where the translated text will be saved.
target_language – Language code for translation (e.g., es for Spanish, fr for French).
Example
To translate data.txt into Spanish (es) and save it to translated_data.txt:

```bash
python translate_script.py data.txt translated_data.txt es
```
Output: The translated content will be written to translated_data.txt.

## 🔍 Code Highlights

✅ **Uses `google-cloud-translate`** – Communicates with **Google Cloud Translation API**.  
✅ **Efficient Processing** – Reads input **line by line** for optimized translation.  
✅ **Handles Empty Lines** – Skips empty lines gracefully.  
✅ **Clean Output** – Outputs **translated text** line by line in the specified language.  

---

## 💡 Ideal Use Cases

✔ **Bulk Text Translation** – Automate translation of large text files.  
✔ **Multilingual Content Processing** – Process documents in multiple languages.  
✔ **Workflow Automation** – Enhance applications needing translation services.  

