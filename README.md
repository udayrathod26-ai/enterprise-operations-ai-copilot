# Enterprise Operations AI Copilot

AI-powered Operations Intelligence platform built using Python, Streamlit, SQL, and Large Language Models to provide business insights through natural language interaction.

## Business Problem

Organizations generate large volumes of operational data across employees, projects, financial metrics, and business activities. Business leaders often rely on manual reporting and analyst support to obtain actionable insights.

Enterprise Operations AI Copilot enables users to ask business questions in natural language and receive AI-generated insights instantly.

## Live Demo: https://enterprise-operations-ai-copilot-b2zkspazmksdhajpbwciaz.streamlit.app/

## Features

* Natural language business queries
* Executive summary generation
* KPI analytics
* Project risk and delay detection
* Resource utilization insights
* Incident/SLA analysis
* Power BI dashboard integration
* Conversational interface

## Tech Stack

Frontend:
- Streamlit

Backend:
- Python

AI:
- OpenAI/Gemini API

Database:
- SQL

Analytics:
- Power BI

Deployment:
- Streamlit Cloud

## Architecture

User Query
      ↓
Question Router
      ↓
Business Query Engine
      ↓
AI Processing Layer
      ↓
Data Analysis
      ↓
Power BI Visualization
      ↓
Response Generation

## Project Structure

Copilot/

├── app.py
├── ai_engine.py
├── business_queries.py
├── chart_generator.py
├── data_loader.py
├── question_router.py
├── screenshots/
├── Power Bi/screenshots/
├── tests/
├── datasets/
└── README.md

## Screenshots

### Home Screen
![Home Screen](screenshots/01_home.png)

### KPI Dashboard
![KPI Dashboard](screenshots/02_kpi_dashboard.png)

### Executive Brief
![Executive Brief](screenshots/03_executive_brief.png)

### Project Performance
![Project Performance](screenshots/04_project_performance.png)

### Business Issues & Risk
![Business Issues](screenshots/05_Business_issues_risk.png)

### Employee Utilization
![Employee Utilization](screenshots/06_Employee_Utilization.png)

### Root Cause Analysis
![Root Cause Analysis](screenshots/07_Root_Cause.png)

### Generative AI Insights
![Generative AI Insights](screenshots/Generative_AI_Insights.png)


### PowerBi Dashboard
### Executive KPI Dashboard
![Dashboard_Overview](PowerBi/screenshots/01_Dashboard_Overview.png)

### Project Delivary & SLA
![Project Delivary & SLA](PowerBi/screenshots/02_Project_Delivery_&_SLA.png)

### Risk & Operations
![Risk & Operations](PowerBi/screenshots/03_Risk_&_Operations.png)

### Resource & Workforce Analytics
![Resource & Workforce Analytics](PowerBi/screenshots/04_Resource_&_Workforce_Analytics.png)

## Future Improvements
* Real-time database integration
* Predictive analytics
* Multi-user authentication
* Agentic workflow automation

## Author
Uday Singh Rathod
