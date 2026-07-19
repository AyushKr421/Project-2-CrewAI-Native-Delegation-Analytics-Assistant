from analytics_mcp_server.mcp_app import mcp


@mcp.tool()
def mcp_generate_report_markdown(
    dataset_summary: dict,
    data_quality_findings: dict,
    recommended_kpis: dict,
    ml_use_cases: dict,
    risks: list,
    next_steps: list,
) -> str:
    """
    Generate a final markdown report.
    """

    report = "# Analytics Report\n\n"

    report += "## Dataset Summary\n\n"
    report += f"```json\n{dataset_summary}\n```\n\n"

    report += "## Data Quality Findings\n\n"
    report += f"```json\n{data_quality_findings}\n```\n\n"

    report += "## Recommended KPIs\n\n"
    report += f"```json\n{recommended_kpis}\n```\n\n"

    report += "## ML Use Cases\n\n"
    report += f"```json\n{ml_use_cases}\n```\n\n"

    report += "## Risks\n\n"

    if risks:
        for risk in risks:
            report += f"- {risk}\n"
    else:
        report += "- No major risks identified.\n"

    report += "\n## Next Steps\n\n"

    if next_steps:
        for i, step in enumerate(next_steps, start=1):
            report += f"{i}. {step}\n"
    else:
        report += (
            "1. Profile the dataset.\n"
            "2. Resolve data quality issues.\n"
            "3. Track KPIs.\n"
            "4. Build ML models.\n"
            "5. Deploy and monitor.\n"
        )

    return report