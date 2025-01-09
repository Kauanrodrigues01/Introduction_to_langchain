from langchain_groq import ChatGroq

from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate, SystemMessagePromptTemplate

from langchain_core.messages import ChatMessage, ChatMessageChunk, HumanMessage, HumanMessageChunk, AIMessage, AIMessageChunk, FunctionMessage, SystemMessage, SystemMessageChunk, ToolMessage, ToolMessageChunk

# Classes de mensagnes principais: SystemMessage, AIMessage, HumanMessage

model = ChatGroq(model='llama-3.3-70b-versatile')

chat_template = ChatPromptTemplate.from_messages(
    messages=[
        SystemMessage(content='Você é um assistente, que deve responder com base em dados geograficos de regiões do Brasil.'),
        HumanMessagePromptTemplate.from_template('Por favor, me fale sobre a região {regiao}.'),
        AIMessage(content='Claro, vou começar coletando informações sobre a região e analisando os dados disponíveis.'),
        HumanMessage(content='Certifique-se de incluir informações sobre a população, clima e economia da região.'),
        AIMessage(content='Entendido, vou incluir essas informações na resposta. Aqui estão os dados que encontrei:'),
    ]
)

prompt = chat_template.format_messages(regiao='Sul')

response = model.invoke(prompt)

print(response.content)