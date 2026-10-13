# Emotion Detector

## Project Overview
Emotion Detector is a Python-based application that analyzes text and identifies emotions using the Watson NLP Emotion Prediction API.

## Features
- Detects anger, disgust, fear, joy, and sadness.
- Identifies the dominant emotion in the input text.
- Provides a web interface using Flask.
- Handles blank inputs and API errors.
- Includes unit testing and static code analysis.

## Technologies Used
- Python
- Watson NLP API
- Flask
- Requests
- Unittest
- Pylint

## Project Structure
```text
Emotion-Detector/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── server.py
├── test_emotion_detection.py
├── requirements.txt
└── README.md
```

## Installation
```bash
git clone <repository-url>
cd Emotion-Detector
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

## Run the Application
```bash
python server.py
```

Open `http://127.0.0.1:5000/` in your browser.

## Run Unit Tests
```bash
python -m unittest -v
```

## Static Code Analysis
```bash
pylint server.py
```

