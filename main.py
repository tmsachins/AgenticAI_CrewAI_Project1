import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool
# from langchain_openai import ChatOpenAI
# from langchain_community.llms import Ollama

load_dotenv()

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
print(os.environ["OPENAI_API_KEY"])
search_tool = SerperDevTool()

# Creating a senior researcher agent with memory and verbose mode
research_agent = Agent(
    role="Senior Researcher",
    goal="Uncover grundbreaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[search_tool],
    allow_delegation=True
)