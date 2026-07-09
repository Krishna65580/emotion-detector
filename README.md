# Emotion Detector

An AI-based web application that analyzes text input and detects the
underlying emotions (anger, disgust, fear, joy, sadness) using the
Watson NLP EmotionPredict service, built with Python and Flask.

## Project Overview

This project was built as the final project for the course
*Developing AI Applications with Python and Flask*. The application:

- Accepts a text statement from the user
- Sends the text to the Watson NLP EmotionPredict service
- Returns the scores for anger, disgust, fear, joy, and sadness
- Identifies and displays the dominant emotion
- Handles blank/invalid input gracefully with a proper error message
- Is deployed as a web application using Flask

## Project Structure

```
.
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py   # Core emotion detection logic
├── static/
│   └── mywebscript.js         # Client-side JS for calling the API
├── templates/
│   └── index.html             # Web UI
├── server.py                  # Flask server and routes
├── test_emotion_detection.py  # Unit tests
├── requirements.txt           # Python dependencies
└── README.md
```

## Setup

1. Clone this repository:
   ```
   git clone <this-repo-url>
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the server:
   ```
   python3 server.py
   ```
4. Open a browser and go to `http://localhost:5000`

## Running Unit Tests

```
python3 -m unittest test_emotion_detection.py
```

## Static Code Analysis

```
pylint server.py EmotionDetection/emotion_detection.py
```

## Author

Krishna
