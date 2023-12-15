import unittest
import pdf_to_audio

test_pdf_path = "./Developer_Jokes.pdf"

# Extract text from the extract_text_from_pdf function
extracted_text = pdf_to_audio.extract_text_from_pdf(test_pdf_path)

class Pdf_to_Speech_TestCase(unittest.TestCase):
    """Tests for PDF to Speech extraction."""

    def test_extract_text_from_pdf(self):
        """Test if text has been extracted from pdf."""

        expected_text = "developers"

        assert expected_text in extracted_text


    def test_pdf_file_is_not_empty(self):
        """Test if the pdf file is not empty and contains text."""

        self.assertTrue(len(extracted_text) > 0)


if __name__ == "__main__":
    unittest.main()