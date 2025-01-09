from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

model = ChatGroq(model='llama-3.3-70b-versatile')


template = '''
Traduza o texto do {idioma1} para o {idioma2}:
{texto}
'''

prompt_template = PromptTemplate.from_template(
    template=template
)

prompt = prompt_template.format(
    idioma1='português',
    idioma2='Alemão',
    texto='Boa noite, tudo bem?'
)

# Observe que o prompt é gerado a partir do template
print(prompt)

print()

response = model.invoke(prompt)
print(f'Resposta: {response.content}')