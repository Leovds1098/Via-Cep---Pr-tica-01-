import requests

url = "https://viacep.com.br/ws/"
uf = "MG"
cidade = "Belo Horizonte"
logradouro = "Rua dos Aimores"
formato = "/json/"

# Monta a URL para consulta por endereço
consulta = f"{url}{uf}/{cidade}/{logradouro}{formato}"

r = requests.get(consulta)

if r.status_code == 200:
    enderecos = r.json()
    print(f"\nForam encontrados {len(enderecos)} resultados:\n")
    for i, endereco in enumerate(enderecos, start=1):
        print(f"Resultado {i}:")
        print(f"  CEP: {endereco.get('cep')}")
        print(f"  Logradouro: {endereco.get('logradouro')}")
        print(f"  Bairro: {endereco.get('bairro')}")
        print(f"  Cidade: {endereco.get('localidade')}")
        print(f"  UF: {endereco.get('uf')}")
        print()
else:
    print("Nao houve sucesso na requisicao.")