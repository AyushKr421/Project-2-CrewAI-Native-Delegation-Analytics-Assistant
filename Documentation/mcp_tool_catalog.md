# MCP Tool Catalog

## Project

CrewAI Native Delegation Analytics Assistant

---

# Overview

This project implements a local **Model Context Protocol (MCP) Server** named **analytics_mcp_server**.

The MCP server provides reusable analytics tools that can be invoked by the Supervisor Agent, Data Analyst Agent, and Data Scientist Agent.

These tools perform dataset profiling, SQL validation, data quality analysis, KPI generation, machine learning recommendations, and report generation.

---

# MCP Server

**Server Name**

```
analytics_mcp_server
```

---

# Available MCP Tools

## 1. mcp_profile_csv

### Purpose

Profiles a CSV dataset and returns basic dataset information.

### Used By

- Data Analyst Agent
- Data Scientist Agent

### Input

```python
csv_file: str
```

### Output

- Number of rows
- Number of columns
- Missing values
- Duplicate rows
- Data types
- Sample records

### Example

```python
mcp_profile_csv("uploaded_dataset.csv")
```

---

## 2. mcp_validate_sql

### Purpose

Validates SQL queries before execution.

### Used By

- Supervisor Agent
- Data Analyst Agent

### Validation Checks

- Read-only query
- SELECT statement
- LIMIT clause
- Avoid SELECT *
- Date filter
- Partition column usage

### Example

```python
mcp_validate_sql("SELECT * FROM sales LIMIT 10")
```

---

## 3. mcp_detect_data_quality_issues

### Purpose

Detects common data quality problems.

### Used By

- Data Analyst Agent
- Data Scientist Agent

### Checks

- Missing values
- Duplicate rows
- Invalid data types
- Negative values
- Outliers
- Constant columns
- High-cardinality columns

### Example

```python
mcp_detect_data_quality_issues("uploaded_dataset.csv")
```

---

## 4. mcp_generate_kpi_catalog

### Purpose

Generates business KPIs based on dataset columns and business domain.

### Used By

- Supervisor Agent
- Data Analyst Agent

### Output

- KPI Name
- Formula
- Business Purpose
- Reporting Frequency

### Example

```python
mcp_generate_kpi_catalog(
    domain="Sales",
    columns=[
        "customer_id",
        "revenue",
        "order_date"
    ]
)
```

---

## 5. mcp_recommend_ml_use_cases

### Purpose

Suggests suitable machine learning use cases based on dataset columns.

### Used By

- Supervisor Agent
- Data Scientist Agent

### Output

- ML Problem Type
- Required Features
- Business Value

### Example

```python
mcp_recommend_ml_use_cases(
    [
        "customer_id",
        "purchase_amount",
        "churn"
    ]
)
```

---

## 6. mcp_generate_report_markdown

### Purpose

Generates a structured Markdown analytics report by combining outputs from multiple MCP tools.

### Used By

- Supervisor Agent

### Report Sections

- Dataset Summary
- Data Quality Findings
- Recommended KPIs
- ML Use Cases
- Risks
- Next Steps

### Example

```python
mcp_generate_report_markdown(
    dataset_summary,
    data_quality_findings,
    recommended_kpis,
    ml_use_cases,
    risks,
    next_steps
)
```

---

# MCP Tool Usage Flow

```
User
   │
   ▼
Supervisor Agent
   │
   ├───────────────┐
   ▼               ▼
Data Analyst   Data Scientist
   │               │
   ▼               ▼
MCP Tools      MCP Tools
   │               │
   └───────┬───────┘
           ▼
Report Generator
           ▼
Final User Response
```

---

# Benefits

- Reusable analytics functions
- Modular architecture
- Easy integration with CrewAI agents
- Improved maintainability
- Consistent analytics workflow
- Scalable tool design

---

# Summary

The **analytics_mcp_server** provides six reusable MCP tools that support data analysis, SQL validation, KPI generation, machine learning recommendations, and automated report generation. These tools enable collaboration between the Supervisor Agent, Data Analyst Agent, and Data Scientist Agent while keeping the application modular and extensible.