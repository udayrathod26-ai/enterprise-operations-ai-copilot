from business_queries import (
    get_delayed_projects,
    get_top_performers,
    get_low_utilization,
    get_critical_incidents,
    get_top_root_causes,
    get_sla_compliance,
    get_executive_brief_data
)


def route_question(question):

    question = question.lower()

    # Delayed / High Risk Projects
    if any(word in question for word in [
        "delay",
        "late",
        "behind schedule",
        "project risk",
        "project performance",
        "high risk",
        "delayed project",
        "at risk project",
        "project status"
    ]):
        return get_delayed_projects()

    # Top Performers
    elif any(word in question for word in [
        "top performer",
        "top performers",
        "top employee",
        "best employee",
        "highest productive",
        "high performer",
        "most productive",
        "best team",
        "best resource"
    ]):
        return get_top_performers()

    # Utilization / Resource Efficiency
    elif any(word in question for word in [
        "low utilization",
        "resource utilization",
        "utilization",
        "resource efficiency",
        "poor resource efficiency",
        "underperforming assets",
        "underutilized",
        "resource usage",
        "employee utilization"
    ]):
        return get_low_utilization()

    # Incidents
    elif any(word in question for word in [
        "critical incident",
        "major occurrence",
        "serious event",
        "incident",
        "business issue",
        "major issue",
        "operational issue",
        "crisis"
    ]):
        return get_critical_incidents()

    # Root Cause Analysis
    elif any(word in question for word in [
        "root cause",
        "root causes",
        "core issues",
        "incident cause",
        "reason",
        "why",
        "problem source",
        "issue analysis"
    ]):
        return get_top_root_causes()

    # SLA
    elif any(word in question for word in [
        "sla",
        "compliance",
        "service level",
        "performance agreement",
        "sla status"
    ]):
        return get_sla_compliance()

    # Executive Brief
    elif any(word in question for word in [
        "executive summary",
        "executive brief",
        "business summary",
        "management summary",
        "overall summary",
        "overall performance"
    ]):
        return get_executive_brief_data()

    else:
        return """
Sorry, I don't understand that question yet.

Try asking:

• Show delayed projects
• Show top performers
• Show employee utilization
• Show critical incidents
• Show root causes
• Show SLA compliance
• Generate executive summary
"""