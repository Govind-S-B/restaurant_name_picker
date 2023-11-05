from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

llm = Ollama(model="zephyr",
             temperature="0.6")


def get_restaurant_name_and_menu(cuisine):
    '''
    Accepts a cuisine name and generates a restaurant name matching that cuisine and a list of menu options for that restaurant
    '''

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

    chain_output = chain({
        "cuisine": cuisine
    })

    return {
        "name": chain_output["restaurant_name"],
        "menu": chain_output["menu_items"]
    }


if __name__ == "__main__":
    print(get_restaurant_name_and_menu("indian"))
