import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

# Use constants for maintaining easily
# Set a time-out constant to avoid freezing
MODEL = "gemini-3.6-flash"
TIMEOUT_MS = 20_000

_client = None


def _get_client():
    global _client
    if _client is None:
        _client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    return _client


def generate_text(prompt: str) -> str:
    response = _get_client().models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            http_options=types.HttpOptions(timeout=TIMEOUT_MS),
        ),
    )

    #.strip() check if the text has multiple spaces
    text = response.text
    if not text or not text.strip():
        raise ValueError("The model returned no usable text.")
    return text
