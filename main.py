from langchain.llms import Ollama

llm = Ollama(model="zephyr",
             temperature="1")

name = llm("I want to open a resturant for French cusine mixed with indian cusine , a fusion style . Suggest a fancy name for this restaurant . The response should be just a single name and nothing else")
print(name)
