from langchain_groq import ChatGroq
from langchain_community.cache import SQLiteCache
from langchain.globals import set_llm_cache

model = ChatGroq(model='llama-3.3-70b-versatile')

set_llm_cache(
    SQLiteCache(database_path='ia_cache.db') # Seta o cache para o SQLiteCache, cria um cache em SQLite
)

prompt = 'Qual a função do framework Django?'

response1 = model.invoke(prompt)
print(f'Chamada 1: {response1.content}')

print()
print('=' * 200)
print()

response2 = model.invoke(prompt)
print(f'Chamada 2: {response2.content}')

# Para testar o cache, execute o script e veja que a resposta da segunda chamada é a mesma da primeira, depois apague o 'ia_cache.db' e ambas as respostas seram diferentes das duas anteriores
