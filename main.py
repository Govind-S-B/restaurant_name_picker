from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

llm = Ollama(model="zephyr",
             temperature="0.6")

cusine_prompt_template = PromptTemplate(
    input_variables=["cuisine "],
    template="""I want to open a restaurant for {cuisine} food. Suggest a fancy name for this restaurant."""
)

restaurant_name_chain = LLMChain(
    llm=llm, prompt=cusine_prompt_template, output_key="restaurant_name")

menu_prompt_template = PromptTemplate(
    input_variables=["restaurant_name"],
    template="""Give a 10 item menu for a restaurant named {restaurant_name}"""
)

restaurant_menu_chain = LLMChain(
    llm=llm, prompt=menu_prompt_template, output_key="menu_items")

chain = SequentialChain(
    chains=[restaurant_name_chain, restaurant_menu_chain],
    input_variables=["cuisine"],
    output_variables=["restaurant_name", "menu_items"])

print(chain({
    "cuisine": "french indian fushion"
}))
