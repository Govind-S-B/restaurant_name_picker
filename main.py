from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SimpleSequentialChain

llm = Ollama(model="zephyr",
             temperature="1")

cusine_prompt_template = PromptTemplate(
    input_variables=["cuisine "],
    template="""I want to open a restaurant for {cuisine} food. Suggest a fancy name for this restaurant.
    The response should be just a single name and nothing else"""
)

restaurant_name_chain = LLMChain(llm=llm, prompt=cusine_prompt_template)

menu_prompt_template = PromptTemplate(
    input_variables=["restaurant_name"],
    template="""Give a 10 item menu for a restaurant named {restaurant_name}.
    The response should be a list of comma seperated values in the format : 
    [item1,item2,item3]"""
)

restaurant_menu_chain = LLMChain(llm=llm, prompt=menu_prompt_template)

chain = SimpleSequentialChain(
    chains=[restaurant_name_chain, restaurant_menu_chain])

print(chain.run("an indian and french fusion cuisine"))
