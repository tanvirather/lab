from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

OLLAMA_URL="http://localhost:11434"
MODEL = "codellama:latest"

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that gives a one-line definition of the word entered by user"),
        ("human", "{user_input} is the word"),
    ]
)

messages = chat_template.format_messages(user_input="Sesquipedalian")
# print(messages)

chatOllama = ChatOllama(model=MODEL,temperature=0)

response = chatOllama.invoke(messages)
# print(response.content)

chain = chat_template | chatOllama | StrOutputParser()
chainResponse = chain.invoke({"user_input": "Onomatopoeia"})
print(chainResponse)