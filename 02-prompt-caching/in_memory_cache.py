from langchain_groq import ChatGroq
from langchain_community.cache import InMemoryCache
from langchain.globals import set_llm_cache

model = ChatGroq(model='llama-3.3-70b-versatile')

set_llm_cache(InMemoryCache()) # Seta o cache para o InMemoryCache, cria um cache em memória

prompt = 'Qual a função do framework Django?'

response1 = model.invoke(prompt)
print(f'Chamada 1: {response1.content}')

print()
print('=' * 200)
print()

response2 = model.invoke(prompt)
print(f'Chamada 2: {response2.content}')

# Para testar o cache, execute o script e veja que a resposta da segunda chamada é a mesma da primeira