import asyncio
from config import SECRETS
from langchain.llms import Clarifai
from langchain import BasePromptTemplate, LLMChain
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain.schema import HumanMessage, SystemMessage, AIMessage
import os
os.environ["LANGCHAIN_TRACING"] = "true" # If you want to trace the execution of the program, set to "true"
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.agents.agent_toolkits import PlayWrightBrowserToolkit
from langchain.tools.playwright.utils import (
    create_async_playwright_browser,
    create_sync_playwright_browser, # A synchronous browser is available, though it isn't compatible with jupyter.
)

# This import is required only for jupyter notebooks, since they have their own eventloop
import nest_asyncio
nest_asyncio.apply()


# This import is required only for jupyter notebooks, since they have their own eventloop
async_browser = create_async_playwright_browser()
browser_toolkit = PlayWrightBrowserToolkit.from_browser(async_browser=async_browser)
tools = browser_toolkit.get_tools()


llm = Clarifai( pat=SECRETS.get("PAT"), user_id=SECRETS.get("USER_ID"), app_id=SECRETS.get("APP_ID"), model_id=SECRETS.get("MODEL_ID"))

agent_chain = initialize_agent(tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True,)

async def ask():
    response = await agent_chain.arun(input="What's the latest xkcd comic about?")
    print(response)


asyncio.run(ask())