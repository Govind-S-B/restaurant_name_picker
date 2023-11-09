from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

llm = Ollama(model="dolphin2.2-mistral",
             temperature="0.6",
             system="You are a very helpful AI assistant")

chain = ConversationChain(llm=llm)

while True:
    print(f"""AI : {chain.run(input("User : "))}""")
