from google import genai
from dotenv import load_dotenv
import streamlit as st
import os

# -----------------------------------
# Load Environment Variables
# -----------------------------------

load_dotenv()

# -----------------------------------
# Gemini Client
# -----------------------------------

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

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

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        error_message = str(e)

        # Quota exceeded
        if "429" in error_message:

            return """
### Executive Insight

⚠️ AI quota limit reached.

The analytics engine and visualizations remain available.

Please review the supporting data and charts below.
"""

        # Internal Gemini error
        elif "500" in error_message:

            return """
### Executive Insight

⚠️ Gemini service is temporarily unavailable.

Please retry after a few moments.
"""

         # Gemini high demand
        elif "503" in error_message:

            return """
### Executive Insight

⚠️ AI service is currently experiencing high demand.

The dashboard analytics and KPI calculations remain available.

Please try again in a few minutes.
"""
        else:

            return f"""
### Executive Insight

⚠️ An unexpected error occurred.

{error_message}
"""


# -----------------------------------
# Executive Brief Generator
# -----------------------------------

@st.cache_data(show_spinner=False)
def generate_executive_brief(data):

    prompt = f"""
You are a CIO-level Executive Operations Advisor.

Analyze the following enterprise KPI data.

Data:
{data}

Create a concise Executive Brief with:

1. Executive Summary
2. Financial Performance
3. Operational Performance
4. Key Risks
5. Recommended Actions

Guidelines:
- Use plain business language
- Use bullet points
- Write currency as ₹538.6M
- Do not split numbers or currency across lines
- Maximum 200 words
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        error_message = str(e)

        if "429" in error_message:

            return """
## Executive Brief

⚠️ AI quota limit reached.

Executive KPI metrics are still available for review.

Please try again later for AI-generated commentary.
"""

        elif "500" in error_message:

            return """
## Executive Brief

⚠️ Gemini service is temporarily unavailable.

Please retry after a few moments.
"""
         # Gemini high demand
        elif "503" in error_message:

            return """
### Executive Insight

⚠️ AI service is currently experiencing high demand.

The dashboard analytics and KPI calculations remain available.

Please try again in a few minutes.
"""
        else:

            return f"""
## Executive Brief

⚠️ An unexpected error occurred.

{error_message}
"""