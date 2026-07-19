import pandas as pd
from analytics_mcp_server.mcp_app import mcp

@mcp.tool()
def mcp_profile_csv(csv_file: str) -> dict:
    """
    Read a CSV file and return profiling information.

    Returns:
    - rows
    - columns
    - missing values
    - duplicate rows
    - data types
    - sample rows
    """

    try:
        df = pd.read_csv(csv_file)

        return {
            "rows": int(df.shape[0]),
            "columns": int(df.shape[1]),
            "missing_values": df.isnull().sum().to_dict(),
            "duplicates": int(df.duplicated().sum()),
            "data_types": {
                col: str(dtype)
                for col, dtype in df.dtypes.items()
            },
            "sample_rows": df.head(5).to_dict(orient="records"),
        }

    except Exception as e:
        return {
            "error": str(e)
        }