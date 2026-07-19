# Demo Script

## Project Name
CrewAI Native Delegation Analytics Assistant

---

## Introduction

This project is a multi-agent analytics assistant built using **CrewAI**, **Streamlit**, **Ollama**, and a **Local MCP Server**.

The system uses three AI agents:

- Supervisor Agent
- Data Analyst Agent
- Data Scientist Agent

The Supervisor Agent receives the user's request, decides which specialist agent should handle it, and combines the final response.

---

# Step 1: Launch the Application

Open a terminal.

Activate the virtual environment.

```bash
.venv\Scripts\activate
```

Start Ollama.

```bash
ollama serve
```

Run the Streamlit application.

```bash
streamlit run app.py
```

The Streamlit application opens in the browser.

---

# Step 2: Upload Dataset

Upload any CSV dataset.

Example:

- Movie_classification.csv
- Movie_regression.csv

The application stores the uploaded dataset for analysis.

---

# Step 3: Ask Questions

### Example 1

```
Summarize the uploaded dataset.
```

Expected Output

- Dataset summary
- Number of rows
- Number of columns
- Missing values
- Numerical columns
- Categorical columns

---

### Example 2

```
Suggest KPIs for a sales company.
```

Expected Output

- Revenue KPI
- Customer KPI
- Sales KPI
- Dashboard recommendations

---

### Example 3

```
Validate the SQL query:

SELECT * FROM sales LIMIT 10;
```

Expected Output

- SQL safety validation
- Warning for SELECT *
- Suggestions for improvement

---

### Example 4

```
Recommend ML use cases for this dataset.
```

Expected Output

- Regression / Classification recommendation
- Suggested ML models
- Evaluation metrics

---

### Example 5

```
Analyze the uploaded dataset.
First profile it.
Identify data quality issues.
Suggest dashboard KPIs.
Recommend ML use cases.
Suggest feature engineering ideas.
Provide a final implementation plan.
```

Expected Output

The Supervisor Agent coordinates the analysis and returns:

- Direct Answer
- Dataset Summary
- Data Quality Findings
- Recommended KPIs
- Dashboard Recommendation
- ML Use Cases
- Feature Engineering Ideas
- Risks
- Next Steps
- Agent Work Summary

---

# Activity Timeline

During execution, the application displays:

- User Message Received
- Context Window Estimated
- Building Ollama LLM
- Creating CrewAI Agents
- Preparing Manager Task
- Calling Function Tool
- Starting Hierarchical Delegation
- Calling MCP Tool
- Tool Result Received
- CrewAI Run Completed
- Final Response Generated

---

# Sidebar Information

The sidebar displays:

- Selected Ollama Model
- Available Agents
- Available Function Tools
- Available MCP Tools
- Context Window Usage
- CrewAI Usage Metrics
- Delegation Trace

---

# Function Tools

### Supervisor Agent

- classify_user_request
- summarize_chat_history
- estimate_context_usage
- create_agent_work_plan
- validate_final_response_structure

### Data Analyst Agent

- profile_dataframe
- suggest_kpi_metrics
- generate_dashboard_layout
- validate_sql_safety
- explain_query_result

### Data Scientist Agent

- recommend_ml_problem_type
- suggest_feature_engineering
- detect_ml_data_risks
- recommend_evaluation_metrics
- create_ml_pipeline_plan

---

# MCP Tools

- mcp_profile_csv
- mcp_validate_sql
- mcp_detect_data_quality_issues
- mcp_generate_kpi_catalog
- mcp_recommend_ml_use_cases
- mcp_generate_report_markdown

---

# Conclusion

The project demonstrates a collaborative multi-agent system where specialized AI agents analyze datasets, recommend business KPIs, suggest machine learning solutions, and generate structured analytics reports using local function tools and MCP tools through a Streamlit interface.