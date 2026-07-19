from analytics_mcp_server.mcp_app import mcp


@mcp.tool()
def mcp_generate_kpi_catalog(domain: str, columns: list) -> dict:
    """
    Generate a KPI catalog based on the business domain and dataset columns.
    """

    domain = domain.lower()

    kpis = []

    if domain == "ecommerce":
        kpis = [
            {
                "name": "Conversion Rate",
                "formula": "orders / sessions",
                "grain": "daily",
                "business_use": "Tracks funnel effectiveness"
            },
            {
                "name": "Average Order Value",
                "formula": "revenue / orders",
                "grain": "daily",
                "business_use": "Measures average customer spend"
            },
            {
                "name": "Revenue",
                "formula": "SUM(revenue)",
                "grain": "daily",
                "business_use": "Tracks total business revenue"
            },
            {
                "name": "Repeat Purchase Rate",
                "formula": "repeat_customers / total_customers",
                "grain": "monthly",
                "business_use": "Measures customer loyalty"
            },
            {
                "name": "Order Cancellation Rate",
                "formula": "cancelled_orders / total_orders",
                "grain": "daily",
                "business_use": "Tracks order cancellations"
            }
        ]

    elif domain == "sales":
        kpis = [
            {
                "name": "Total Sales",
                "formula": "SUM(sales)",
                "grain": "daily",
                "business_use": "Measures total sales revenue"
            },
            {
                "name": "Sales Growth",
                "formula": "(Current - Previous) / Previous",
                "grain": "monthly",
                "business_use": "Measures business growth"
            },
            {
                "name": "Average Deal Size",
                "formula": "sales / deals",
                "grain": "monthly",
                "business_use": "Measures average deal value"
            },
            {
                "name": "Customer Acquisition Rate",
                "formula": "new_customers / total_customers",
                "grain": "monthly",
                "business_use": "Tracks customer growth"
            }
        ]

    elif domain == "finance":
        kpis = [
            {
                "name": "Net Profit",
                "formula": "Revenue - Expenses",
                "grain": "monthly",
                "business_use": "Measures profitability"
            },
            {
                "name": "Gross Margin",
                "formula": "(Revenue - Cost) / Revenue",
                "grain": "monthly",
                "business_use": "Measures operating efficiency"
            },
            {
                "name": "ROI",
                "formula": "Profit / Investment",
                "grain": "quarterly",
                "business_use": "Measures investment return"
            }
        ]

    else:
        kpis = [
            {
                "name": "Revenue",
                "formula": "SUM(value)",
                "grain": "daily",
                "business_use": "Tracks business performance"
            },
            {
                "name": "Growth Rate",
                "formula": "(Current - Previous) / Previous",
                "grain": "monthly",
                "business_use": "Measures business growth"
            }
        ]

    return {
        "domain": domain,
        "available_columns": columns,
        "kpis": kpis
    }