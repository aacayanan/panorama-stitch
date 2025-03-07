from openai import OpenAI
import base64
from dotenv import load_dotenv

image_path = 'stitched.jpeg'
load_dotenv()

# Encode the image to a base64 string
with open(image_path, 'rb') as img:
    img_base64 = base64.b64encode(img.read()).decode('utf-8')

# Create a new OpenAI object
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{img_base64}"
                    }
                }
            ]
        }
    ],
    max_tokens=300,
)

print(response.choices[0].message.content)
