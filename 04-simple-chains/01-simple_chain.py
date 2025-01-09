from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser # Utilizando o StrOutputParser para obter a resposta como string, evitando ter que usar o "response.content", vamos colocar ele em um chain(que é uma sequência de funções que são executadas em ordem)

model = ChatGroq(model='llama-3.3-70b-versatile')

prompt_template = PromptTemplate.from_template(
    "Me fale sobre o carro {carro}.",
)

runnable_sequence = prompt_template | model | StrOutputParser() # Cria um chain com o prompt_template, model e StrOutputParser

response = runnable_sequence.invoke({'carro': 'Uno mille'})

print(response)


# Para testar os chains, brinque de trocar os prompts templates, use outros parsers e etc... 