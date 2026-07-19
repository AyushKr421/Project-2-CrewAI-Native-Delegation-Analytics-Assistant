import re
from analytics_mcp_server.mcp_app import mcp


@mcp.tool()
def mcp_validate_sql(sql_query: str, partition_column: str = "event_date") -> dict:
    """
    Validate SQL query safety before execution.

    Checks:
    - Read-only query
    - LIMIT clause
    - Avoid SELECT *
    - Date filter
    - Partition column usage
    """

    query = sql_query.strip()
    query_lower = query.lower()

    warnings = []
    safe = True

    # --------------------------------------------------
    # 1. Read-only query
    # --------------------------------------------------
    forbidden = [
        "insert",
        "update",
        "delete",
        "drop",
        "alter",
        "truncate",
        "create",
        "replace",
        "merge"
    ]

    for keyword in forbidden:
        if re.search(rf"\b{keyword}\b", query_lower):
            safe = False
            warnings.append(f"Forbidden SQL operation detected: {keyword.upper()}")

    # --------------------------------------------------
    # 2. Must be SELECT
    # --------------------------------------------------
    if not query_lower.startswith("select"):
        safe = False
        warnings.append("Only SELECT queries are allowed.")

    # --------------------------------------------------
    # 3. LIMIT check
    # --------------------------------------------------
    if "limit" not in query_lower:
        warnings.append("LIMIT clause is missing.")

    # --------------------------------------------------
    # 4. Avoid SELECT *
    # --------------------------------------------------
    if re.search(r"select\s+\*", query_lower):
        warnings.append("Avoid using SELECT *. Specify required columns.")

    # --------------------------------------------------
    # 5. Date filter check
    # --------------------------------------------------
    if "where" not in query_lower:
        warnings.append("No WHERE clause found.")

    if not any(
        word in query_lower
        for word in ["date", "event_date", "order_date", "timestamp"]
    ):
        warnings.append("No date filter detected.")

    # --------------------------------------------------
    # 6. Partition column check
    # --------------------------------------------------
    if partition_column.lower() not in query_lower:
        warnings.append(
            f"Partition column '{partition_column}' is not used."
        )

    return {
        "safe": safe,
        "query_type": "SELECT" if query_lower.startswith("select") else "UNKNOWN",
        "warnings": warnings
    }