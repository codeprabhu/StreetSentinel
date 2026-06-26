from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

with open("pothole.jpg", "rb") as f:
    image_bytes = f.read()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/jpeg",
        ),
        """
        Analyze this image.

        Return ONLY valid JSON:

        {
            "issue_type": "",
            "severity": "",
            "description": "",
            "impact_score": 0
        }
        """
    ]
)

print(response.text)