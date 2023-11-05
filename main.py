from langchain.llms import Ollama
from langchain.prompts import PromptTemplate

llm = Ollama(model="zephyr",
             temperature="1")

cusine_prompt_template = PromptTemplate(
    input_variables=["cuisine "],
    template="""I want to open a resturant for {cuisine}. Suggest a name for this restaurant.
    The response should be just a single name and nothing else"""
)

name = llm("I want to open a resturant for French cusine mixed with indian cusine , a fusion style . Suggest a fancy name for this restaurant . The response should be just a single name and nothing else")
print(name)
