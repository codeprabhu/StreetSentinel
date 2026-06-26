from google import genai
from google.genai import types # type: ignore
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))


PROMPT = """
You are StreetSentinel's Infrastructure Assessment Agent.

Analyze the uploaded image.

Possible issue types:
- Pothole
- Road Crack
- Water Leakage
- Garbage Overflow
- Damaged Streetlight
- Obstruction
- Other

Return ONLY valid JSON:

{
  "issue_type": "",
  "severity": "",
  "description": "",
  "impact_score": 0,
  "recommended_department": "",
  "recommended_action": ""
}
"""


def analyze_image(image_path):
    print("Detector called")
    print("Image path:", image_path)
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    
    response = client.models.generate_content(
        model = "gemini-2.0-flash",
        contents = [
            types.Part.from_bytes(
                data=image_bytes,
                mime_type = "image/jpg"
            ),
            PROMPT
        ]
    )

    return response.text