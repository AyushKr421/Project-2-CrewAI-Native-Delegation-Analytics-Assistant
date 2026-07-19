import os
import sys

from mcp import StdioServerParameters
from crewai_tools import MCPServerAdapter


def get_mcp_tools():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[
            "-m",
            "analytics_mcp_server.server",
        ],
        env={**os.environ},
    )

    adapter = MCPServerAdapter(server_params)

    return adapter, adapter.tools