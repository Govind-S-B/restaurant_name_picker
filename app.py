import streamlit as st
import langchain_helper

st.title("Restaurant Idea Generator")

cuisine = st.sidebar.selectbox("Pick a cuisine", options=[
                               "Indian", "Italian", "Mexican", "French", "Japanese"])

if cuisine:
    response = langchain_helper.get_restaurant_name_and_menu(cuisine)
    st.header(response["name"])
    st.write("### Menu")
    for item in response["menu"]:
        st.write(f"- {item}")
