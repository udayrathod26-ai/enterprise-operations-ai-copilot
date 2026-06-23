from business_queries import (get_delayed_projects,
    get_top_performers,
    get_low_utilization,
    get_critical_incidents,
    get_top_root_causes,
    get_sla_compliance,
    get_executive_brief_data)

def route_question(question):
    question = question.lower()
    if ("delay" in question
        or "late" in question
        or "behind schedule" in question):
        return get_delayed_projects()
    
    elif( "top performer" in question
         or "topper" in question
         or "best employee" in question
         or "highest productive" in question):
        return get_top_performers()
    
    elif ("low utilization" in question          
         or "low throughput" in question
         or "poor resource efficiency" in question
         or "underperforming assets" in question):
        return get_low_utilization()

    elif ("critical incident" in question
          or "major occurrence" in question
          or "serious event" in question
          or "key crisis" in question          
          ):
        return get_critical_incidents()

    elif("root cause" in question
          or "core issues" in question
          or "incident cause" in question
          or "why" in question
          ):
        return get_top_root_causes()

    elif "sla" in question:
        return get_sla_compliance()

    elif "executive summary" in question:
        return get_executive_brief_data()

    else:
        return "Sorry, I don't understand that question yet."
    