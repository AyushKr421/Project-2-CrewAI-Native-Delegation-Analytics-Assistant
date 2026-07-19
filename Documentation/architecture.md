# System Architecture

## Overview

The CrewAI Native Delegation Analytics Assistant is a multi-agent system that uses CrewAI, Streamlit, Ollama, and a local MCP Server to perform business analytics and machine learning recommendations on uploaded CSV datasets.

The application follows a hierarchical architecture where the Supervisor Agent manages the workflow and delegates work to specialist agents.

---

# High Level Architecture

```
                   +----------------------+
                   |      User            |
                   +----------+-----------+
                              |
                              |
                              v
                  +------------------------+
                  |     Streamlit UI       |
                  +-----------+------------+
                              |
                              |
                              v
                  +------------------------+
                  |   Supervisor Agent     |
                  +-----------+------------+
                              |
                +-------------+-------------+
                |                           |
                |                           |
                v                           v
      +------------------+        +--------------------+
      | Data Analyst     |        | Data Scientist     |
      | Agent            |        | Agent              |
      +--------+---------+        +---------+----------+
               |                            |
               |                            |
               v                            v
      +------------------+        +----------------------+
      | Function Tools   |        | Function Tools       |
      +--------+---------+        +---------+------------+
               |                            |
               +-------------+--------------+
                             |
                             v
                 +--------------------------+
                 | Local MCP Server         |
                 +------------+-------------+
                              |
          +-------------------+-------------------+
          |                   |                   |
          v                   v                   v
   CSV Profiling       SQL Validation     Data Quality
          |
          +-------------------------------------------+
                              |
                              v
                     KPI Generation
                              |
                              v
                    ML Use Case Recommendation
                              |
                              v
                   Markdown Report Generator
                              |
                              v
                  +--------------------------+
                  |   Final User Response    |
                  +--------------------------+
```

---

# Components

## 1. Streamlit UI

The Streamlit application provides the user interface for interacting with the analytics assistant.

Responsibilities:

- Upload CSV datasets
- Accept user questions
- Display responses
- Display activity timeline
- Display CrewAI metrics
- Display delegation trace
- Show available tools

---

## 2. Supervisor Agent

The Supervisor Agent acts as the manager of the analytics team.

Responsibilities:

- Understand user intent
- Review previous chat history
- Select the appropriate specialist agent
- Delegate work
- Validate responses
- Combine specialist outputs
- Return the final answer

---

## 3. Data Analyst Agent

The Data Analyst Agent focuses on business analytics.

Responsibilities:

- Dataset profiling
- Data quality analysis
- KPI recommendation
- Dashboard recommendation
- SQL validation
- Business insights
- Trend explanation

---

## 4. Data Scientist Agent

The Data Scientist Agent focuses on machine learning.

Responsibilities:

- ML problem identification
- Feature engineering suggestions
- Data risk detection
- Evaluation metric recommendation
- ML pipeline planning
- Model strategy recommendation

---

# Function Tools

## Supervisor Function Tools

- classify_user_request
- summarize_chat_history
- estimate_context_usage
- create_agent_work_plan
- validate_final_response_structure

---

## Data Analyst Function Tools

- profile_dataframe
- suggest_kpi_metrics
- generate_dashboard_layout
- validate_sql_safety
- explain_query_result

---

## Data Scientist Function Tools

- recommend_ml_problem_type
- suggest_feature_engineering
- detect_ml_data_risks
- recommend_evaluation_metrics
- create_ml_pipeline_plan

---

# MCP Server

The local MCP Server exposes reusable analytics tools.

Implemented MCP Tools:

- mcp_profile_csv
- mcp_validate_sql
- mcp_detect_data_quality_issues
- mcp_generate_kpi_catalog
- mcp_recommend_ml_use_cases
- mcp_generate_report_markdown

---

# Workflow

### Step 1

The user uploads a CSV dataset.

↓

### Step 2

The user submits a query.

↓

### Step 3

The Supervisor Agent analyzes the request.

↓

### Step 4

The Supervisor delegates the task to the Data Analyst Agent, Data Scientist Agent, or both.

↓

### Step 5

The specialist agents invoke local function tools and MCP tools.

↓

### Step 6

The generated insights are returned to the Supervisor Agent.

↓

### Step 7

The Supervisor Agent combines the responses into a structured report.

↓

### Step 8

The Streamlit application displays the final response along with the activity timeline and execution metrics.

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Agent Framework | CrewAI |
| LLM | Ollama (llama3.2:3b) |
| MCP Server | FastMCP |
| Data Processing | Pandas |
| Configuration | YAML |
| Programming Language | Python |

---

# Safety Controls

The application includes several safety mechanisms:

- SQL query validation
- CSV file validation
- File extension checking
- File size limitation
- Safe exception handling
- Restricted local file access
- Hidden debug logs

---

# Benefits of the Architecture

- Modular design
- Multi-agent collaboration
- Easy tool extensibility
- Reusable MCP services
- Scalable analytics workflow
- Separation of responsibilities
- Clear delegation process
- Easy maintenance