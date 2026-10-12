"""Call the Watson NLP emotion-prediction service and format its response."""

from typing import Any, Dict, Optional

import requests

EMOTION_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
TIMEOUT_SECONDS = 20


def emotion_detector(text: str) -> Optional[Dict[str, Any]]:
    """Return five emotion scores and the dominant emotion.

    Returns None when the service responds with HTTP 400. Other request,
    JSON-decoding, or response-shape errors are allowed to be handled by the
    caller, so that the web layer can return a useful error message.
    """
    if not isinstance(text, str) or not text.strip():
        return None

    headers = {"grpc-metadata-mm-model-id": MODEL_ID}
    payload = {"raw_document": {"text": text}}

    response = requests.post(
        EMOTION_URL,
        headers=headers,
        json=payload,
        timeout=TIMEOUT_SECONDS,
    )

    if response.status_code == 400:
        return None

    response.raise_for_status()
    result = response.json()
    emotions = result["emotionPredictions"][0]["emotion"]

    scores = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }
    scores["dominant_emotion"] = max(
        ("anger", "disgust", "fear", "joy", "sadness"),
        key=scores.get,
    )
    return scores
