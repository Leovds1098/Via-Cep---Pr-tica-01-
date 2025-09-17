import requests

url = 'https://viacep.com.br/ws/'
cep_inicial = 30140071
formato = '/xml/'

for i in range(5):  # gera 5 CEPs sequenciais
    cep = str(cep_inicial + i)
    r = requests.get(url + cep + formato)

    if r.status_code == 200:
        print(f'\nResultado para o CEP {cep}:')
        print(r.text)  # mostra o XML retornado
    else:
        print(f'\nNao houve sucesso na requisicao para o CEP {cep}.')