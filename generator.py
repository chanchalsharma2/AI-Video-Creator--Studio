import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_video_content(topic, duration, tone):
    # Direct command for JSON-like structured output
    prompt = f"""
    RETURN ONLY A JSON-FORMATTED OBJECT. NO PROSE. NO GREETINGS.
    
    INPUT_DATA:
    {{
        "topic": "{topic}",
        "duration": "{duration}",
        "tone": "{tone}"
    }}
    
    SCHEMA_REQUIRED:
    {{
        "viral_titles": [],
        "video_script": {{
            "hook": "",
            "intro": "",
            "main_content": [],
            "outro": ""
        }},
        "seo_metadata": {{
            "description": "",
            "tags": []
        }}
    }}
    """
    
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a raw data generator. Return content strictly in valid JSON format. Do not provide any conversational text."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.2 # Lower temperature for more stable/robotic output
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"{{'error': '{str(e)}'}}"