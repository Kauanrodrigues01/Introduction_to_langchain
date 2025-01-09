from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGroq(model='llama-3.3-70b-versatile')


chain = (
    PromptTemplate.from_template(
        "Me fale sobre o carro {carro}."
    )
    | model
    | StrOutputParser()
)

response = chain.invoke({'carro': 'Uno mille'})

print(response)
