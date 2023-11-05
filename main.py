from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(model="zephyr",
             temperature="1")

cusine_prompt_template = PromptTemplate(
    input_variables=["cuisine "],
    template="""I want to open a resturant for {cuisine} food. Suggest a fancy name for this restaurant.
    The response should be just a single name and nothing else"""
)

chain = LLMChain(llm=llm, prompt=cusine_prompt_template)
print(chain.run("an indian and french fusion cuisine"))
