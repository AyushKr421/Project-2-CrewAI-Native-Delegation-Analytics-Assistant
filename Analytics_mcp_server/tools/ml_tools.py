from analytics_mcp_server.mcp_app import mcp


@mcp.tool()
def mcp_recommend_ml_use_cases(columns: list) -> dict:
    """
    Recommend machine learning use cases based on dataset columns.
    """

    cols = [col.lower() for col in columns]

    ml_use_cases = []

    # ---------------------------------------------------------
    # Churn Prediction
    # ---------------------------------------------------------
    if (
        "customer_id" in cols
        and ("churn" in cols or "churn_label" in cols)
    ):
        ml_use_cases.append({
            "use_case": "Customer Churn Prediction",
            "problem_type": "classification",
            "required_columns": [
                "customer_id",
                "activity_count",
                "churn_label"
            ],
            "business_value": "Reduce customer loss by identifying customers likely to leave."
        })

    # ---------------------------------------------------------
    # Sales Prediction
    # ---------------------------------------------------------
    if (
        "sales" in cols
        or "revenue" in cols
        or "price" in cols
    ):
        ml_use_cases.append({
            "use_case": "Sales Forecasting",
            "problem_type": "forecasting",
            "required_columns": [
                "date",
                "sales"
            ],
            "business_value": "Forecast future sales for better inventory and planning."
        })

    # ---------------------------------------------------------
    # Fraud Detection
    # ---------------------------------------------------------
    if (
        "transaction_id" in cols
        or "amount" in cols
    ):
        ml_use_cases.append({
            "use_case": "Fraud Detection",
            "problem_type": "classification",
            "required_columns": [
                "transaction_id",
                "amount",
                "fraud_label"
            ],
            "business_value": "Detect fraudulent transactions before financial loss occurs."
        })

    # ---------------------------------------------------------
    # Customer Segmentation
    # ---------------------------------------------------------
    if (
        "customer_id" in cols
        and (
            "age" in cols
            or "income" in cols
            or "purchase_amount" in cols
        )
    ):
        ml_use_cases.append({
            "use_case": "Customer Segmentation",
            "problem_type": "clustering",
            "required_columns": [
                "customer_id",
                "age",
                "income",
                "purchase_amount"
            ],
            "business_value": "Group similar customers for personalized marketing."
        })

    # ---------------------------------------------------------
    # Recommendation System
    # ---------------------------------------------------------
    if (
        "customer_id" in cols
        and "product_id" in cols
    ):
        ml_use_cases.append({
            "use_case": "Product Recommendation",
            "problem_type": "recommendation",
            "required_columns": [
                "customer_id",
                "product_id",
                "rating"
            ],
            "business_value": "Recommend relevant products to increase sales."
        })

    # ---------------------------------------------------------
    # House Price Prediction
    # ---------------------------------------------------------
    if (
        "price" in cols
        and (
            "area" in cols
            or "bedrooms" in cols
        )
    ):
        ml_use_cases.append({
            "use_case": "House Price Prediction",
            "problem_type": "regression",
            "required_columns": [
                "area",
                "bedrooms",
                "price"
            ],
            "business_value": "Predict property prices for buyers and sellers."
        })

    # ---------------------------------------------------------
    # Default Case
    # ---------------------------------------------------------
    if not ml_use_cases:
        ml_use_cases.append({
            "use_case": "Exploratory Data Analysis",
            "problem_type": "analysis",
            "required_columns": columns,
            "business_value": "Analyze the dataset to identify potential ML opportunities."
        })

    return {
        "ml_use_cases": ml_use_cases
    }