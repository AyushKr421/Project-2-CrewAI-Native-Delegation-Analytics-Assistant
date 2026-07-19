from crewai import Agent
from function_tools.scientist_tools import (
    recommend_ml_problem_type,
    suggest_feature_engineering,
    detect_ml_data_risks,
    recommend_evaluation_metrics,
    create_ml_pipeline_plan,
)


def create_data_scientist_agent(
    agents_config,
    llm,
    step_callback,
    mcp_tools=None,
):
    """
    Creates the Data Scientist Agent from agents.yaml
    """

    config = agents_config["data_scientist_agent"]

    local_tools = [
        recommend_ml_problem_type,
        suggest_feature_engineering,
        detect_ml_data_risks,
        recommend_evaluation_metrics,
        create_ml_pipeline_plan,
    ]

    data_scientist_agent = Agent(
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

    return data_scientist_agent