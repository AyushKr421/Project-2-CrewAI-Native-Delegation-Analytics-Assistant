from analytics_mcp_server.tools.csv_profile_tools import mcp_profile_csv
from analytics_mcp_server.tools.sql_tools import mcp_validate_sql
from analytics_mcp_server.tools.data_quality_tools import (
    mcp_detect_data_quality_issues,
)
from analytics_mcp_server.tools.kpi_tools import (
    mcp_generate_kpi_catalog,
)
from analytics_mcp_server.tools.ml_tools import (
    mcp_recommend_ml_use_cases,
)
from analytics_mcp_server.tools.report_tools import (
    mcp_generate_report_markdown,
)


print("\n===== MCP TOOL TESTS =====\n")

# -----------------------------
# Test 1 : CSV Profiling
# -----------------------------
print("Test 1 : CSV Profiling")
print(mcp_profile_csv("uploaded_dataset.csv"))


# -----------------------------
# Test 2 : SQL Validation
# -----------------------------
print("\nTest 2 : SQL Validation")
print(mcp_validate_sql("SELECT * FROM sales LIMIT 10"))


# -----------------------------
# Test 3 : Data Quality
# -----------------------------
print("\nTest 3 : Data Quality")
print(mcp_detect_data_quality_issues("uploaded_dataset.csv"))


# -----------------------------
# Test 4 : KPI Catalog
# -----------------------------
print("\nTest 4 : KPI Catalog")
print(
    mcp_generate_kpi_catalog(
        domain="Sales",
        columns=[
            "customer_id",
            "revenue",
            "order_date",
            "product"
        ]
    )
)


# -----------------------------
# Test 5 : ML Use Cases
# -----------------------------
print("\nTest 5 : ML Use Cases")
print(
    mcp_recommend_ml_use_cases(
        [
            "customer_id",
            "activity_count",
            "churn",
            "purchase_amount"
        ]
    )
)


# -----------------------------
# Test 6 : Markdown Report
# -----------------------------
print("\nTest 6 : Markdown Report")

print(
    mcp_generate_report_markdown(
        dataset_summary={"rows": 100, "columns": 5},
        data_quality_findings={"missing": 2},
        recommended_kpis={"kpis": ["Revenue", "Profit"]},
        ml_use_cases={"use_cases": ["Churn Prediction"]},
        risks=["Missing Values"],
        next_steps=[
            "Clean Data",
            "Build Dashboard",
            "Train Model",
        ],
    )
)