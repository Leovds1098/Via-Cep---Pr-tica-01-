import requests

url = 'https://viacep.com.br/ws/'
cep = '30140071'
formato = '/xml/'  # alterado para XML
r = requests.get(url + cep + formato)

if r.status_code == 200:
    print()
    print('XML : ')
    print(r.text)  # exibe o XML como texto
    print()
else:
    print('Nao houve sucesso na requisicao.')