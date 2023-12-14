from PyPDF2 import PdfReader
from gtts import gTTS

def extract_text_from_pdf(file_to_read):
    """
    Extracts and combines text from all pages of a given PDF file.

    Arguments:
    file_to_read (str): Path to the PDF file to be read.

    Returns:
    str: Combined text extracted from the PDF. 
    """

    combined_text = ""

    with open(file_to_read, "rb") as pdf_to_read:

        # Create a PDF reader object to interpret the file
        pdf_reader = PdfReader(pdf_to_read)

        # Iterate through each page in the PDF
        for page in pdf_reader.pages:

            # Extract text from the current page
            extracted_text = page.extract_text()

            # If text was found, concatenate it to the combined text
            if extracted_text:
                combined_text += extracted_text + "\n"
    
    return combined_text


def convert_text_to_speech(text, audio_file_name):
    """
    Converts the text into an audio file and saves it.

    Arguments: 
    text (str): The text to be converted to speech.
    audio_file_name (str): The name of the output audio file, including the file extension (e.g., '.mp3').

    Returns:
    Saves the audio to a file.
    """

    language = "en"

    # Create an audio with the specified language and speed settings
    audio = gTTS(text=text, lang=language, slow=False)

    audio.save(audio_file_name)

