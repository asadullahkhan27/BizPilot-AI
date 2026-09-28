import os
import requests

from dotenv import load_dotenv


load_dotenv()


def ask_ai(prompt):

    api_key = os.getenv(
        "GROQ_API_KEY",
        ""
    ).strip()

    model = os.getenv(
        "GROQ_MODEL",
        "llama-3.3-70b-versatile"
    ).strip()

    if not api_key:

        return """
AI is not configured.

Add GROQ_API_KEY to your .env file.

The rest of BizPilot AI will continue working
without the AI API.
"""

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {

        "model": model,

        "messages": [

            {
                "role": "system",

                "content": """
You are BizPilot AI, a business operations
analyst.

Analyze only the business data provided by
the user.

Do not invent missing information.

Clearly distinguish:
- facts
- observations
- assumptions

Provide practical business insights.
"""
            },

            {
                "role": "user",
                "content": prompt
            }

        ],

        "temperature": 0.2
    }

    try:

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=60
        )

        response.raise_for_status()

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as error:

        return f"""
AI request failed.

Error:
{error}
"""
