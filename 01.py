from langchain_groq import ChatGroq

model = ChatGroq(model='llama-3.3-70b-versatile')

messages = [
    {'role': 'system', 'content': 'Você é um assistente que fornece informações sobre figuras históricas. Seu nome é Whend, e quando perguntarem seu nome, você deve responder "Whend", podendo adicionar um complemento caso queira.'},
    {'role': 'user', 'content': 'Qual é o seu nome?'},
    {'role': 'ai', 'content': 'Meu nome é whend, seu assistente.'},
    {'role': 'user', 'content': 'Quem foi Cristiano Ronaldo? Certifique-se de limitar sua resposta em 100 tokens'}
]

response = model.invoke(
    messages,
    max_tokens=100,
    temperature=1
)

print(response.content)
