import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": 4},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": 4},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": 4},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": 4}
]

model = genai.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings
)

# --- Functions ---
def ai(prompt):
  print(prompt)
  response = model.generate_content(prompt)
  while(True):
    if response._done:
      return(response.text)
