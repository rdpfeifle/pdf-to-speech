# PDF to Speech

This project includes functionality to extract text from PDF files and then use text-to-speech technology to generate audible versions of the content, enhancing accessibility and convenience.

## Features

- Extract text from a given PDF
- Convert extracted text to audio

## Technologies

- **Python**: The programming language used for the project.
- **PyPDF2 library**: Utilized for extracting text from PDF files.
- **gTTS library**: Google Text-to-Speech, used for converting extracted text to audio format.

## Motivation

I enjoy reading, but sometimes it's hard to get into the mood to tackle certain PDF documents, especially lengthy or complex ones. That's where the idea for this tool came in: Why not create a way to convert these PDFs into audio? With this approach, I can access the necessary information in a more relaxed and convenient manner, either by just listening or by combining audio with traditional reading.

## Instructions

### Installation

```
virtualenv env
source env/bin/activate

pip3 install -r requirements.txt
```

### Running the code

```
python3 pdf_to_audio.py
```

## License

© 2023 Raquel Pfeifle. All Rights Reserved. This project is licensed under the [MIT License](LICENSE).

## Contact

Raquel Pfeifle - [LinkedIn](https://www.linkedin.com/in/raqueldpfeifle)
