from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader # Necessita instalar o pypdf: pip install pypdf

model = ChatGroq(model='llama-3.3-70b-versatile')

loader = PyPDFLoader(file_path='07-loaders/dados/base_conhecimento.pdf')
documents = loader.load() # Retorna uma lista das paginas do documento

print('DOCUMENTS:\n', documents)

prompt_base_conhecimento = PromptTemplate(
    input_variables=['document_content', 'pergunta'],
    template="""
    Use o seguinte conteúdo do documento para responder à pergunta. 
    Responda apenas com base nas informações fornecidas.
    Não utilize informações externas ao conteúdo do documento:
    Conteúdo do Documento: {document_content}
    Pergunta: {pergunta} 
    """
)

chain = prompt_base_conhecimento | model | StrOutputParser()

response = chain.stream(
    {
        'document_content': '\n'.join(doc.page_content for doc in documents),
        'pergunta': 'Qual o conteúdo do arquivo?'
    }
)

print('\nRESPONSE:\n')

for chuck in response:
    print(chuck, end='')