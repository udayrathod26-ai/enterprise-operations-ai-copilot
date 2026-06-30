import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import os

# -----------------------------------
# Load Environment Variables
# -----------------------------------

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("GOOGLE_API_KEY not found")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

# -----------------------------------
# Business Question Summary
# -----------------------------------

@st.cache_data(show_spinner=False)
def generate_summary(question, data):

    prompt = f"""
You are an AI Operations Copilot for an enterprise organization.

Question:
{question}

Data:
{data}

Analyze the data and provide:

Executive Insight:
- A concise business summary

Key Findings:
- Important observations
- Risks or opportunities

Management Action:
- Recommended next steps

Keep the response:
- Professional
- Executive-focused
- Under 150 words
- Use bullet points where appropriate
"""

    try:

        response = model.generate_content(prompt)

        if response and hasattr(response, "text"):
            return response.text

        return "⚠️ No response received from Gemini."

    except Exception as e:

        error_message = str(e)

        if "429" in error_message:
            return """
### Executive Insight

⚠️ AI quota limit reached.

Dashboard analytics remain available.
"""

        elif "500" in error_message:
            return """
### Executive Insight

⚠️ Gemini service temporarily unavailable.
"""

        elif "503" in error_message:
            return """
### Executive Insight

⚠️ Gemini service experiencing high demand.

Please try again shortly.
"""

        return f"""
### Executive Insight

⚠️ Error:

{error_message}
"""


# -----------------------------------
# Executive Brief Generator
# -----------------------------------

@st.cache_data(show_spinner=False)
def generate_executive_brief(data):

    prompt = f"""
You are a CIO-level Executive Operations Advisor.

Analyze:

{data}

Create:

1. Executive Summary
2. Financial Performance
3. Operational Performance
4. Key Risks
5. Recommended Actions

Maximum 200 words.
"""

    try:

        response = model.generate_content(prompt)

        if response and hasattr(response, "text"):
            return response.text

        return "⚠️ No response received from Gemini."

    except Exception as e:

        error_message = str(e)

        if "429" in error_message:
            return """
## Executive Brief

⚠️ AI quota limit reached.
"""

        elif "500" in error_message:
            return """
## Executive Brief

⚠️ Gemini temporarily unavailable.
"""

        elif "503" in error_message:
            return """
## Executive Brief

⚠️ High service demand.

Please retry in a few minutes.
"""

        return f"""
## Executive Brief

⚠️ Error:

{error_message}
"""