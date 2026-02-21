from pathlib import Path
import os
from dotenv import load_dotenv
from deepagents import create_deep_agent
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from langchain_community.utilities import SQLDatabase
load_dotenv(override=True)

system_prompt = (Path(__file__).parent / "AGENTS.md").read_text()

_engine = create_engine(
    URL.create("mssql+pyodbc", query={"odbc_connect": os.environ["MSSQL_CONNECTION_STRING"]})
)
db = SQLDatabase(_engine)


def create_chomi_agent():
    """Create a Chomi agent."""
    return create_deep_agent(
        model="openai:gpt-4o",
        tools=[],
        system_prompt=system_prompt,
    )


def main():
    print(f"Dialect: {db.dialect}")
    print(f"Available tables: {db.get_usable_table_names()}")
    print(f'Sample output: {db.run("SELECT * FROM [Lebenkele].[dbo].[Customers]")}')


if __name__ == "__main__":
    main()
