import streamlit as st

st.title("Restaurant Idea Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", options=[
                               "Indian", "Italian", "Mexican", "French", "Japanese"])


def get_restaurant_name_and_menu(cuisine):
    '''
    Accepts a cuisine name and generates a restaurant name matching that cuisine and a list of menu options for that restaurant
    '''

    return {
        "name": "cafe bistro",
        "menu": ["falafel", "samosa", "chicken nuggets"]
    }


if cuisine:
    response = get_restaurant_name_and_menu("Indian")
    st.header(response["name"])
    st.write("### Menu")
    for item in response["menu"]:
        st.write(f"- {item}")
