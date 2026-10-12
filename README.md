# Watson NLP Emotion Detector

A Python package and Flask web application that sends text to the Watson NLP
EmotionPredict service and formats the five emotion scores: anger, disgust,
fear, joy, and sadness. It also reports the dominant emotion.

## Project structure

```text
Emotion_Detector_Project/
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── test_emotion_detection.py
├── server.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or later
- Internet access to the course-provided Watson NLP endpoint
- pip

## Setup

From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1`.

## Test package import

```bash
python -c "from EmotionDetection import emotion_detector; print('Package import successful')"
```

## Run unit tests

The unit tests mock the HTTP service, so they do not require the external Watson
endpoint to be reachable:

```bash
python -m unittest -v
```

## Run the Flask application

```bash
python server.py
```

Open http://127.0.0.1:5000 in a browser. Enter a sentence and select **Analyze
emotion**. Blank input is rejected before a service request is made.

The service endpoint is the course-hosted endpoint configured in
`EmotionDetection/emotion_detection.py`. If the host is unreachable from your
network, live predictions cannot be produced until connectivity is restored.
Do not present mocked unit-test values as real Watson predictions.

## Test the HTTP endpoint

With the server running, open:

```text
http://127.0.0.1:5000/emotionDetector?textToAnalyze=I%20am%20happy
```

Blank-input validation can be tested with:

```text
http://127.0.0.1:5000/emotionDetector?textToAnalyze=
```

The second request should return HTTP 400 and a readable validation message.

## Static code analysis

Run Pylint against the requested Flask file:

```bash
python -m pylint server.py
```

Save the terminal output or take a screenshot that clearly shows the command and
the final score. Pylint scores depend on the installed Pylint version and its
active configuration; do not claim a 10/10 score unless the command actually
reports it. Fix reported issues and rerun the command.

## GitHub submission URLs

After creating a **public** repository and pushing these files, replace
`YOUR_GITHUB_USERNAME` and `YOUR_REPOSITORY` below with your actual values.

- Task 1 README: `https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/blob/main/README.md`
- Task 4 package initializer: `https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY/blob/main/EmotionDetection/__init__.py`

## Rubric evidence checklist

1. **Task 1:** Submit the public URL to `README.md`.
2. **Task 2, Activity 1:** Show `EmotionDetection/emotion_detection.py`.
3. **Task 2, Activity 2:** Show terminal output for importing the package and testing the function. Include a real live-service result only if the endpoint is reachable.
4. **Task 3, Activity 1:** Show the returned five scores and `dominant_emotion` in `emotion_detection.py`.
5. **Task 3, Activity 2:** Show output containing all five scores and the dominant emotion.
6. **Task 4, Activity 1:** Submit the public URL to `EmotionDetection/__init__.py`.
7. **Task 4, Activity 2:** Show a successful package import command/output.
8. **Task 5, Activity 1:** Show `test_emotion_detection.py`.
9. **Task 5, Activity 2:** Show the terminal output from `python -m unittest -v` with all tests passing.
10. **Task 6, Activity 1:** Show `server.py`.
11. **Task 6, Activity 2:** Save a screenshot of the running web application as `6b_deployment_test.png`.
12. **Task 7, Activity 1:** Show the HTTP 400 handling in `emotion_detection.py`.
13. **Task 7, Activity 2:** Show blank-input validation in `server.py`.
14. **Task 7, Activity 3:** Save a screenshot of the blank-input error interface as `7c_error_handling_interface.png`.
15. **Task 8, Activity 1:** Show `server.py` and the command used to run Pylint.
16. **Task 8, Activity 2:** Submit a terminal screenshot showing the actual Pylint score. The rubric asks for a perfect score; verify the displayed result rather than editing or fabricating terminal output.

## Notes

This is a starter implementation for the course assignment. Keep the course's
required endpoint and model ID intact. Check the assignment's expected output
wording and adapt the interface if your evaluator requires exact text.
