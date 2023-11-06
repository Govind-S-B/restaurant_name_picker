import json
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

llm = Ollama(model="zephyr",
             temperature="0.6")

llm_mistral = Ollama(model="mistral",
                     temperature="0.2")


def get_restaurant_name_and_menu(cuisine):
    '''
    Accepts a cuisine name and generates a restaurant name matching that cuisine and a list of menu options for that restaurant
    '''

    # name generation chain

    cusine_prompt_template = PromptTemplate(
        input_variables=["cuisine "],
        template="""I want to open a restaurant for {cuisine} food. Suggest a fancy name for this restaurant."""
    )

    restaurant_name_chain = LLMChain(
        llm=llm, prompt=cusine_prompt_template, output_key="restaurant_name")

    # name clean up chain

    name_clean_up_template = PromptTemplate(
        input_variables=["restaurant_name"],
        template="""from the following text, extract a name for an restaurant, it should just be a single name and nothing more.
        When given multiple options choose the best one that feels catchy and fancy but only one should be given.


    {restaurant_name}
    """
    )

    restaurant_name_clean_up_chain = LLMChain(
        llm=llm_mistral, prompt=name_clean_up_template, output_key="cleaned_name")

    # menu generation chain

    menu_prompt_template = PromptTemplate(
        input_variables=["cleaned_name"],
        template="""Give a 10 item menu for a restaurant named {cleaned_name}"""
    )

    restaurant_menu_chain = LLMChain(
        llm=llm, prompt=menu_prompt_template, output_key="menu_items")

    # menu clean up chain

    menu_clean_up_template = PromptTemplate(
        input_variables=["menu_items"],
        template="""from the following text, extract a list of comma seperated values for the menu items for an restaurant.
        it should strictly be in the format specified. Ignore any category titles ,only extract the menu items in the list

    {menu_items}
    """
    )

    restaurant_menu_clean_up_chain = LLMChain(
        llm=llm_mistral, prompt=menu_clean_up_template, output_key="cleaned_menu")

    chain = SequentialChain(
        chains=[restaurant_name_chain, restaurant_name_clean_up_chain,
                restaurant_menu_chain, restaurant_menu_clean_up_chain],
        input_variables=["cuisine"],
        output_variables=["restaurant_name", "cleaned_name", "menu_items", "cleaned_menu"])

    chain_output = chain({
        "cuisine": cuisine
    })

    return {
        "name": chain_output["restaurant_name"],
        "clean_name": chain_output["cleaned_name"],
        "menu": chain_output["menu_items"],
        "cleaned_menu": chain_output["cleaned_menu"]
    }


if __name__ == "__main__":
    data = get_restaurant_name_and_menu("indo french fusion")
    print(json.dumps(data, indent=4))
