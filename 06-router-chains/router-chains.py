from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatGroq(model='llama-3.3-70b-versatile')

classification_chain = (
    PromptTemplate.from_template(
        '''
        Classifique a pergunta do usuario em uma das seguintes setores:
        - Financeiro
        - Suporte Técnico
        - Outras Informações
        
        Se a pergunta se encaixar em um dos setores, retorne uma resposta com o nome do setor em que a pergunta se encaixa. Problemas de acesso, como senha, devem ser classificados como Suporte Técnico.
        
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

# Cada chain pode ter um modelo especifico, ou seja, o modelo pode ser treinado para responder perguntas de um setor especifico

financial_chain = (
    PromptTemplate.from_template(
        ''''
        Você é um especialista financeiro.
        Sempre responda às perguntas começando com "Bem-vindo ao Setor Financeiro".
        Responda à pergunta do usuário:
        Pergunta: {pergunta}
        '''
    )
    | model
    | StrOutputParser()
)

tech_support_chain = (
    PromptTemplate.from_template(
        """
        Você é um especialista em suporte técnico.
        Sempre responda às perguntas começando com "Bem-vindo ao Suporte Técnico".
        Responda à pergunta do usuário:
        Pergunta: {pergunta}
        """
    )
    | model
    | StrOutputParser() 
)

other_info_chain = (
    PromptTemplate.from_template(
        """
        Você é um assistente de informações gerais.
        Sempre responda às perguntas começando com "Bem-vindo ao setor de Central de Informações".
        Responda à pergunta do usuário:
        Pergunta: {pergunta}
        """
    )
    | model
    | StrOutputParser() 
)


def route(topic):
    if 'Financeiro' in topic or 'financeiro' in topic:
        return financial_chain
    elif 'Técnico' in topic or 'técnico' in topic:
        return tech_support_chain
    else:
        return other_info_chain
    

pergunta : str = input('Qual a sua pergunta? \n')
    
classification = classification_chain.invoke({'pergunta': pergunta})

print()

response_chain = route(classification)

response = response_chain.invoke({'pergunta': pergunta})

print(response)