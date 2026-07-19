from crewai import Agent
from function_tools.analyst_tools import (
    profile_dataframe,
    suggest_kpi_metrics,
    generate_dashboard_layout,
    validate_sql_safety,
    explain_query_result,
)


def create_data_analyst_agent(
    agents_config,
    llm,
    step_callback,
    mcp_tools=None,
):
    """
    Creates the Data Analyst Agent from agents.yaml
    """

    config = agents_config["data_analyst_agent"]

    local_tools = [
        profile_dataframe,
        validate_sql_safety,
        suggest_kpi_metrics,
        generate_dashboard_layout,
        explain_query_result,
    ]

    data_analyst_agent = Agent(
        role=config["role"],
        goal=config["goal"],
        backstory=config["backstory"],
        verbose=config.get("verbose", True),
        allow_delegation=config.get("allow_delegation", False),
        max_iter=config.get("max_iter", 2),
        max_retry_limit=config.get("max_retry_limit", 2),
        llm=llm,
        step_callback=step_callback,
        tools=local_tools + (mcp_tools or []),
    )

    return data_analyst_agent