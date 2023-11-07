from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import Ollama

# from langchain.tools import Tool, DuckDuckGoSearchRun, ArxivQueryRun, WikipediaQueryRun
# from langchain.utilities import WikipediaAPIWrapper
# from langchain.agents import initialize_agent
# from langchain.agents import AgentType
# from langchain.chat_models import ChatOpenAI
# from langchain.chains import LLMChain
# from langchain.prompts import PromptTemplate

llm = Ollama(model="dolphin2.2-mistral",
             temperature="0.2")

tools = load_tools(["llm-math", "ddg-search"], llm=llm)

agent = initialize_agent(
    tools, llm, AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

print(agent.run("how old is elon musk going to be at the year 2030"))
