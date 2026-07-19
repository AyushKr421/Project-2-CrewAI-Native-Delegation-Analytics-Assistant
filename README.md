# CrewAI Native Delegation Analytics Assistant

## Project Overview

This project is a multi-agent analytics assistant developed using **CrewAI**, **Streamlit**, **Ollama**, and a **local MCP (Model Context Protocol) Server**.

The application demonstrates how multiple AI agents collaborate to solve analytics and machine learning tasks through native delegation.

The system contains three specialized agents:

- Supervisor Agent
- Data Analyst Agent
- Data Scientist Agent

The application allows users to upload a CSV dataset and ask analytics questions. Based on the request, the Supervisor Agent delegates work to the appropriate specialist agent(s), combines their responses, and returns a structured answer.

---

# Features

- Multi-Agent Architecture using CrewAI
- Native Hierarchical Delegation
- Local MCP Server
- CSV Dataset Upload
- Dataset Profiling
- Data Quality Detection
- KPI Recommendation
- Dashboard Recommendation
- SQL Validation
- ML Use Case Recommendation
- Feature Engineering Suggestions
- Final Markdown Report
- Live Activity Timeline
- Sidebar Metrics
- Context Window Estimation

---

# Project Structure

```
CrewAI_Native_Delegation/

│
├── agents/
│   ├── supervisor_agent.py
│   ├── data_analyst_agent.py
│   └── data_scientist_agent.py
│
├── analytics_mcp_server/
│   ├── server.py
│   ├── sample_data/
│   └── tools/
│       ├── csv_profile_tools.py
│       ├── data_quality_tools.py
│       ├── sql_tools.py
│       ├── kpi_tools.py
│       ├── ml_tools.py
│       └── report_tools.py
│
├── function_tools/
│   ├── supervisor_tools.py
│   ├── analyst_tools.py
│   └── scientist_tools.py
│
├── config/
│   ├── agents.yaml
│   └── tasks.yaml
│
├── tests/
│
├── docs/
│
├── app.py
│
└── README.md
```

---

# Agents

## 1. Supervisor Agent

Responsibilities

- Understand user request
- Review conversation
- Decide delegation strategy
- Delegate to specialist agents
- Combine responses
- Return final answer

---

## 2. Data Analyst Agent

Responsibilities

- Dataset Profiling
- SQL Validation
- KPI Suggestion
- Dashboard Recommendation
- Business Insights
- Trend Explanation

---

## 3. Data Scientist Agent

Responsibilities

- ML Problem Recommendation
- Feature Engineering
- Data Quality Detection
- Evaluation Metrics
- ML Pipeline Planning
- Model Strategy

---

# Function Tools

## Supervisor Tools

- classify_user_request
- create_agent_work_plan
- summarize_chat_history
- validate_final_response_structure
- estimate_context_usage

---

## Data Analyst Tools

- profile_dataframe
- suggest_kpi_metrics
- generate_dashboard_layout
- validate_sql_safety
- explain_query_result

---

## Data Scientist Tools

- recommend_ml_problem_type
- suggest_feature_engineering
- detect_ml_data_risks
- recommend_evaluation_metrics
- create_ml_pipeline_plan

---

# MCP Tools

The local MCP Server provides reusable analytics tools.

Implemented MCP Tools

1. mcp_profile_csv
2. mcp_validate_sql
3. mcp_detect_data_quality_issues
4. mcp_generate_kpi_catalog
5. mcp_recommend_ml_use_cases
6. mcp_generate_report_markdown

---

# Technologies Used

- Python
- CrewAI
- Streamlit
- Ollama
- FastMCP
- Pandas
- YAML

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Start Ollama

```bash
ollama serve
```

Pull model

```bash
ollama pull llama3.2:3b
```

Run MCP Server

```bash
python -m analytics_mcp_server.server
```

Run Streamlit

```bash
streamlit run app.py
```

---

# Example Queries

Example 1

```
Summarize the uploaded dataset.
```

Example 2

```
Identify data quality issues.
```

Example 3

```
Suggest dashboard KPIs.
```

Example 4

```
Recommend ML use cases.
```

Example 5

```
Analyze the uploaded dataset and provide an implementation plan.
```

---

# Safety Features

- SQL Query Validation
- CSV File Validation
- Upload Size Restriction
- Restricted File Access
- Hidden Debug Logs
- Safe Exception Handling

---

# Deliverables

- Streamlit Application
- Three CrewAI Agents
- agents.yaml
- tasks.yaml
- Function Tools
- MCP Server
- MCP Tools
- Sample Dataset
- Architecture Documentation
- Test Cases
- README

---

# Future Improvements

- Better Native Delegation
- Support Multiple Datasets
- Interactive Dashboards
- Automatic Visualization
- Cloud Deployment
- Authentication
- Advanced ML Pipelines

---

# Authors

Developed as part of the **ML & Agentic AI Project** using **CrewAI**, **Ollama**, **FastMCP**, and **Streamlit**.