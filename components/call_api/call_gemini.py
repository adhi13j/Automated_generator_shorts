import os
import google.generativeai as genai

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not set in environment variables.")

print("Gemini key loaded successfully.")

model = genai.GenerativeModel("gemini-pro")

def call_gemini(user_ideas, niche , memory):
    prompt = f"""
    Generate a list of YouTube Shorts ideas for the niche: "{niche}".

    If user-provided ideas are given (see below), include them directly in the final idea list (improve phrasing if needed) and generate more ideas of a similar kind to expand the list.

    User Ideas (if any):
    {user_ideas or 'None'}

    Output:
    - A single merged list of ideas
    - Phrase all items concisely and in short-form content style
    - Avoid duplicating or overly rephrasing the user ideas
    - dont not merge with memory
    - answer only the list with no extra characters

    these ideas are already present in memory try to exclude them in your output 
    {memory or 'None'}
    """

    response = model.generate_content(prompt)

    return response