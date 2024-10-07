import requests

def buscar_todos():
    url = 'https://jsonplaceholder.typicode.com/posts'

    #Como fazer uma requisição em uma API com python
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        #Como converter a resposta para json\Dicionário
        dados = response.json()
        for post in dados:
            print(post['title'])
            print(post['body'])
            print('-'*50)

def buscar_por_id():
    print('\n' * 10)
    id = input('Digite o id do post: ')
    url = f'https://jsonplaceholder.typicode.com/posts/{id}'

    response = requests.get(url)

    if response.status_code == 200:
        resultado = response.json()
        print('--- Resultado ---')
        print(f"Titulo: {resultado['title']}")
        print('---------------------------------')
        print(f"Conteúdo: {resultado['body']}")

def add_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    dados = {
        "title":"Post cadastrado",
        "body":"Conteúdo do post",
        "userId":1
    }
    #Enviando uma requisição via Post
    response = requests.post(url, json=dados)
    if response.status_code == 201:
        print('Dados cadastrados com sucesso')
        print(response.json())

def edit_post():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    dados = {
        'title':'Titulo editado',
        'body':'body editado',
        'userId':1
    }
    response = requests.put(url, json=dados)
    if response.status_code == 200:
        print('Dados editados com sucesso')
        print(response.json())

def delete_post():
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    response = requests.delete(url)
    if response.status_code == 200:
        print('Deletado com sucesso')
        print(response.json())

delete_post()