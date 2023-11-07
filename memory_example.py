from langchain.llms import Ollama
from langchain.schema.messages import SystemMessage, HumanMessage


llm = Ollama(model="dolphin2.2-mistral",
             temperature="0.6")

print(llm.invoke([SystemMessage(content="You are a rude newyork resident who speaks only in street slang"),
      HumanMessage(content="whats the weather like")]))
