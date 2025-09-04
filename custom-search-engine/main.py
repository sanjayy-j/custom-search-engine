from exa_py import Exa

exa = Exa('e54894b5-f1a9-46b8-9b70-2acd7d1a5bec')

query = input('Search here: ')

response = exa.search(
    query,                    
    num_results=5,            
    type='keyword',            
    include_domains=['https://www.instagram.com'], 
)

for result in response.results:
    print(f'Title: {result.title}')
    print(f'URL: {result.url}')
    print()
