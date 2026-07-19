from analytics_mcp_server.mcp_app import mcp

# Import all tool modules
from analytics_mcp_server.tools.csv_profile_tools import *
from analytics_mcp_server.tools.sql_tools import *
from analytics_mcp_server.tools.data_quality_tools import *
from analytics_mcp_server.tools.kpi_tools import *
from analytics_mcp_server.tools.ml_tools import *
from analytics_mcp_server.tools.report_tools import *

if __name__ == "__main__":
    mcp.run()