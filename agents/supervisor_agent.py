from crewai import Agent


def create_supervisor_agent(
    agents_config,
    llm,
    step_callback,
):
    """
    Creates the Supervisor Agent from agents.yaml
    """

    config = agents_config["supervisor_agent"]

    supervisor_agent = Agent(
        role=config["role"],
        goal=config["goal"],
        backstory=config["backstory"],
        verbose=config.get("verbose", True),
        allow_delegation=config.get("allow_delegation", True),
        max_iter=config.get("max_iter", 2),
        max_retry_limit=config.get("max_retry_limit", 2),
        llm=llm,
        step_callback=step_callback,
        tools=[]
    )

    return supervisor_agent