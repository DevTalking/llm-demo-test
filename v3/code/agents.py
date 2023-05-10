import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.agents import load_tools
from langchain.agents import create_csv_agent

#os.environ['OPENAI_API_KEY'] = "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"
#os.environ['SERPAPI_API_KEY'] = "17ebf2e02f3f554e07660077c591dac14e90bd3cdbca7fa10494b13f6508c186"
llm = OpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY'])
tool_names = ["serpapi"]
tools = load_tools(tool_names)
google_agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
#csv_agent= create_csv_agent(OpenAI(temperature=0, openai_api_key=os.environ['OPENAI_API_KEY']), './data/titanic.csv', verbose=True)

