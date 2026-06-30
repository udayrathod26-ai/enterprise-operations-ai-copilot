# creating business queries 
from data_loader import (projects,
                         employees,
                         tasks,
                         incidents,
                         timesheets
                         )

# Identifying the delayed projects
def get_delayed_projects():

    result = (
        tasks
        .groupby("project_id")["delay_days"]
        .sum()
        .reset_index()
        .sort_values("delay_days", ascending=False)
    )

    result = result.merge(
        projects[["project_id","project_name"]],
        on="project_id",
        how="left"
    )

    return result.head(10)

#Identifying the top performers
def get_top_performers():
    employee_perf = (timesheets.groupby("employee_id")["productivity_score"]
                     .mean()
                     .reset_index())
    employee_perf = employee_perf.merge(employees[["employee_id","employee_name"]], on = "employee_id", how = "left")
    return (employee_perf.sort_values("productivity_score", ascending = False)
            .head(10)
            )
# Identifying low utilization employees
def get_low_utilization():
    util = (timesheets.groupby("employee_id")["utilization_percentage"]
             .mean()
             .reset_index())
    util = util.merge(employees[["employee_id","employee_name"]], on = "employee_id", how = "left")
    return (util.sort_values("utilization_percentage", ascending = True)
            .head(10)
            )

# Identifying Critical incidents
def get_critical_incidents():
    return incidents[incidents["severity"] == "Critical"]

# Identifying the Top root causes for incidents
def get_top_root_causes():
    return(incidents.groupby("root_cause")
           .size()
           .reset_index(name="incident_count")
           .sort_values("incident_count", ascending=False
            )
    )

#Calculate the SLA complaince
def get_sla_compliance():
    total = len(tasks)  # Gives the total no. of rows in tasks table
    compliant = len(tasks[tasks["sla_breach"]=="No"])
    compliance = (compliant / total) * 100
    return round(compliance,2)

def get_executive_kpis():
    total_revenue = timesheets["billing_amount_inr"].sum()
    total_cost = timesheets["cost_to_company_inr"].sum()
    total_profit = total_revenue - total_cost
    profit_margin = round((total_profit / total_revenue) * 100,2) if total_revenue > 0 else 0

    avg_productivity = round(timesheets["productivity_score"].mean(),2)

    avg_utilization = round(timesheets["utilization_percentage"].mean(),2)

    avg_revenue_per_project = round(total_revenue /projects["project_id"].nunique(), 2)

    return {
        "Total Revenue": float(round(total_revenue/1000000,2)),
        "Total Cost": float(round(total_cost/1000000,2)),
        "Total Profit": float(round(total_profit/1000000,2)),
        "Profit Margin %": float(round(profit_margin,2)),
        "Avg Revenue Per Project": float(round(avg_revenue_per_project/1000000,2)),
        "Avg Productivity": float(round(avg_productivity,2)),
        "Avg Utilization": float(round(avg_utilization,2))
        }


#Generate the Executive summary metrics
def get_executive_brief_data():
    kpis = get_executive_kpis()
    delayed_tasks = int((tasks["delay_days"] > 0).sum())
    critical_incidents = int(len(incidents[incidents["severity"] == "Critical" ]))
    sla_compliance = get_sla_compliance()
    return {
        **kpis,
        "Delayed Tasks": delayed_tasks,
        "Critical Incidents": critical_incidents,
        "SLA Compliance %": sla_compliance
    }
def get_project_revenue():

    revenue_df = projects.groupby("ProjectName", as_index=False)["Revenue"].sum()
    revenue_df = revenue_df.sort_values(by="Revenue",ascending=False)
    revenue_df["Revenue"] = (revenue_df["Revenue"]/1000000 ).round(2)
    revenue_df.rename(  columns={  "Revenue":"Revenue (Millions)"},inplace=True)
    return revenue_df
