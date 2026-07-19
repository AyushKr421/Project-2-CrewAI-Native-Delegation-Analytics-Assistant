import pandas as pd
from analytics_mcp_server.mcp_app import mcp

@mcp.tool()
def mcp_detect_data_quality_issues(csv_file: str) -> dict:
    """
    Detect common data quality issues in a CSV file.

    Checks:
    - Missing values
    - Duplicate rows
    - Invalid data types
    - Negative values in positive-only numeric columns
    - Outliers (IQR Method)
    - Constant columns
    - High-cardinality columns
    """

    try:
        df = pd.read_csv(csv_file)

        report = {}

        # -------------------------------------------------
        # Missing Values
        # -------------------------------------------------
        report["missing_values"] = df.isnull().sum().to_dict()

        # -------------------------------------------------
        # Duplicate Rows
        # -------------------------------------------------
        report["duplicate_rows"] = int(df.duplicated().sum())

        # -------------------------------------------------
        # Invalid Data Types
        # -------------------------------------------------
        report["data_types"] = {
            col: str(dtype)
            for col, dtype in df.dtypes.items()
        }

        # -------------------------------------------------
        # Negative Values (for numeric columns)
        # -------------------------------------------------
        negative_columns = {}

        numeric_cols = df.select_dtypes(include="number").columns

        for col in numeric_cols:
            count = int((df[col] < 0).sum())
            if count > 0:
                negative_columns[col] = count

        report["negative_values"] = negative_columns

        # -------------------------------------------------
        # Outliers (IQR Method)
        # -------------------------------------------------
        outliers = {}

        for col in numeric_cols:

            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1

            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR

            count = int(((df[col] < lower) | (df[col] > upper)).sum())

            if count > 0:
                outliers[col] = count

        report["outliers"] = outliers

        # -------------------------------------------------
        # Constant Columns
        # -------------------------------------------------
        constant_columns = []

        for col in df.columns:
            if df[col].nunique(dropna=False) == 1:
                constant_columns.append(col)

        report["constant_columns"] = constant_columns

        # -------------------------------------------------
        # High Cardinality Columns
        # (>50 unique values)
        # -------------------------------------------------
        high_cardinality = {}

        for col in df.columns:

            unique_count = int(df[col].nunique())

            if unique_count > 50:
                high_cardinality[col] = unique_count

        report["high_cardinality_columns"] = high_cardinality

        return report

    except Exception as e:
        return {
            "error": str(e)
        }