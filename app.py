#### The below program was to create radio buttions to work with AI co pilot 
# import streamlit as st

# from business_queries import ( get_executive_summary, get_delayed_projects, get_top_performers, 
#                               get_low_utilization, get_critical_incidents, get_top_root_causes, get_sla_compliance, )

# st.title( "Operations AI Copilot")

# if st.button("Executive Summary Metrics"):
#     st.dataframe(get_executive_summary())
    
# if st.button("Delayed Projects"):
#     st.dataframe(get_delayed_projects())

# if st.button("Top Performers"):
#     st.dataframe(get_top_performers())

# if st.button("Low Utilization Employees"):
#     st.dataframe(get_low_utilization())

# if st.button("Critical Incidents"):
#     st.dataframe(get_critical_incidents())

# if st.button("Top Root Causes"):
#     st.dataframe(get_top_root_causes())

# if st.button("SLA Compliance"):
#     st.write(get_sla_compliance())

### The below program introduces the concept of AI. That is it replaces the radio button with Chat Box
### where a manager can ask question to see the project performance

# import streamlit as st
# from ai_engine import generate_summary
# import pandas as pd
# from question_router import route_question
# st.title("Operations AI Copilot")
# question = st.text_input("Ask a business question")
# if st.button("Submit"):
#     result = route_question(question)
#     if isinstance(result, pd.DataFrame):
#         summary = generate_summary(
#         question,
#         result.to_string(index=False) )
#         st.subheader("Executive Insight")
#         st.write(summary)

#         st.dataframe(result)

#     else:
#         st.write(result)

### Using generative AI to answer the questions

import streamlit as st
import pandas as pd

from chart_generator import show_chart
from ai_engine import (generate_summary, generate_executive_brief )
from question_router import route_question
from business_queries import (get_executive_kpis, get_executive_brief_data)


# -----------------------------------
# Helper Function
# -----------------------------------

def format_million(value):
    return f"₹{value/1000000:.2f} M"


# -----------------------------------
# Page Title
# -----------------------------------

st.set_page_config(
    page_title="Operations AI Copilot",
    layout="wide"
)

st.title("🤖 Operations AI Copilot")


# -----------------------------------
# Executive KPI Cards
# -----------------------------------

kpis = get_executive_kpis()
st.subheader("Executive Overview")
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue",format_million(kpis["Total Revenue"]))
col2.metric("Total Cost",format_million(kpis["Total Cost"]))
col3.metric("Total Profit", format_million(kpis["Total Profit"]))

col4, col5, col6 = st.columns(3)
col4.metric("Profit Margin %", f"{kpis['Profit Margin %']}%")
col5.metric( "Avg Utilization %", f" {kpis['Avg Utilization']}%")
col6.metric( "Revenue / Project", format_million(kpis["Avg Revenue Per Project"]))

st.divider()
if st.button("📋 Generate Executive Brief"):
    executive_data = get_executive_brief_data()

    with st.spinner("Generating Executive Brief..."):
        brief = generate_executive_brief(str(executive_data))

    st.subheader("📑 Executive Brief")
    st.markdown(brief)

    with st.expander("View Supporting Metrics"):
        col1, col2, col3 = st.columns(3)
        col1.metric("Revenue", f"₹{executive_data['Total Revenue']/1000000:.2f} M")
        col2.metric("Profit", f"₹{executive_data['Total Profit']/1000000:.2f} M")
        col3.metric("Profit Margin", f"{executive_data['Profit Margin %']}%")

        col4, col5, col6 = st.columns(3)
        col4.metric("Utilization", f"{executive_data['Avg Utilization']}%")
        col5.metric("Critical Incidents", executive_data["Critical Incidents"])
        col6.metric("SLA Compliance", f"{executive_data['SLA Compliance %']}%")

st.divider()

# -----------------------------------
# AI Toggle
# -----------------------------------

use_ai = st.checkbox(
    "Generate AI Insights",
    value=True
)


# -----------------------------------
# Question Input
# -----------------------------------

question = st.text_input(
    "Ask a business question"
)


# -----------------------------------
# Process Question
# -----------------------------------

if st.button("Submit"):

    result = route_question(question)

    # -----------------------------------
    # DataFrame Results
    # -----------------------------------

    if isinstance(result, pd.DataFrame):

        if use_ai:

            with st.spinner("Generating AI Insight..."):

                summary = generate_summary(
                    question,
                    result.head(10).to_string(index=False)
                )

            st.subheader("🤖 Operations Copilot Insight")
            st.markdown(summary)

        st.subheader("📈 Visualization")
        show_chart(question, result)

        st.subheader("📊 Supporting Data")
        st.dataframe(
            result,
            use_container_width=True,
            hide_index=True
        )

    # -----------------------------------
    # Dictionary Results
    # -----------------------------------

    elif isinstance(result, dict):

        if use_ai:

            summary = generate_summary(
                question,
                str(result)
            )

            st.subheader("🤖 Operations Copilot Insight")
            st.markdown(summary)

        st.json(result)

    # -----------------------------------
    # Other Results
    # -----------------------------------

    else:

        st.write(result)

    st.success("Analysis completed successfully.")