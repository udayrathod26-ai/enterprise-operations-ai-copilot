import streamlit as st
import plotly.express as px


def show_chart(question, df):

    question = question.lower()

    # -------------------------
    # Delayed Projects
    # -------------------------
    if "delay" in question:

        df = df.sort_values(
        by="delay_days",
        ascending=True
        )
        fig = px.bar(
            df,
            x="delay_days",
            y="project_name",
            orientation="h",
            title="Delayed Projects"
        )

        st.plotly_chart(fig, use_container_width=True)

    # -------------------------
    # Top Performers
    # -------------------------
    elif "performer" in question:

        fig = px.bar(
            df,
            x="productivity_score",
            y="employee_name",
            orientation="h",
            title="Top Performers"
        )

        st.plotly_chart(fig, use_container_width=True)

    # -------------------------
    # Low Utilization
    # -------------------------
    elif "utilization" in question:

        fig = px.bar(
            df,
            x="utilization_percentage",
            y="employee_name",
            orientation="h",
            title="Low Utilization Employees"
        )

        st.plotly_chart(fig, use_container_width=True)

    # -------------------------
    # Root Causes
    # -------------------------
    elif "root cause" in question:

        fig = px.pie(
            df,
            names="root_cause",
            values="incident_count",
            title="Root Cause Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)