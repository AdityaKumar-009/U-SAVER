# U-Saver: YouTube Video Downloader

U-Saver (derived from YouTube Video Saver) is a Python-based YouTube Video Downloader application built using the tkinter library for the user interface. It allows users to easily download YouTube videos by providing a video URL, downloading videos using keywords, or even through voice recognition. The app features different themes for user interface with both light and dark modes.

## Features

- **YouTube URL Video Download**: Users can input a YouTube video URL into the Entry Box and download the video by clicking the "Download" button.

- **AI Video Download**: Users can type a keyword in the second entry box and use the "AI Button" to download the first YouTube video related to the search keyword.

- **Voice Recognition**: U-Saver supports voice recognition, allowing users to initiate video downloads by speaking the keyword into their microphone.

- **Themed UI**: The app offers custom themes, allowing users to switch between light and dark modes to suit their preferences.

- **Version 2.0 Enhancements**:
  - **Progress Bar**: U-Saver now displays a progress bar during video downloads, depicting the file size and download progress.
  - **Multiple Resolutions**: Users can choose from various resolutions (e.g., 144p, 360p, 720p) or even download the video as an MP3 audio file.
  - **Video Thumbnail**: The app now displays a video thumbnail to give users a preview of the content.
  - **Download Confirmation Popup**: Before downloading a video, a confirmation popup will appear, allowing users to confirm or cancel the download.

## Usage
### Installation

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/AdityaKumar-009/U-SAVER.git
   
2. Before running U-Saver, ensure you have the following dependencies installed:
   
   - [python 3.10+](https://www.python.org/downloads/): Python 3.10 or above.
   - [pytube](https://pypi.org/project/pytube/): A Python library for downloading YouTube videos.
   - [PyAudio](https://pypi.org/project/PyAudio/): Required for voice recognition and audio processing.
   - [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): Used for voice recognition.
   - [Pillow](https://pypi.org/project/Pillow/): Used for storing video thumbnail image (required for version 2.0).

       ```bash
       pip install pytube PyAudio SpeechRecognition Pillow

3. Open the project in PyCharm or your preferred Python IDE.

4. Locate and run the U-SAVER.py file to start the U-Saver application.
   
   - Example: for U-SAVER version 1.0
     - locate to folder [U-SAVER 1.0/CODE/U-SAVER.py](https://github.com/AdityaKumar-009/U-SAVER/blob/0c22f4fd4423cd25661c9d437dc4193b1b01ad65/U-SAVER%201.0/CODE/U-SAVER.py)
   - Similarly, for U-SAVER version 2.0
     - locate to folder [U-SAVER 2.0/U-SAVER_2.0.py](https://github.com/AdityaKumar-009/U-SAVER/blob/0c22f4fd4423cd25661c9d437dc4193b1b01ad65/U-SAVER%202.0/U-SAVER_2.0.py)

## License

This project is licensed under the MIT License.

## Disclaimer

Please note that U-Saver was initially created as a college project during my first semester, and it represents my exploration of Python and related technologies at that time.

Happy video downloading with U-Saver!
