import requests

url = "https://viacep.com.br/abc/"

r = requests.get(url)

print("Código de retorno:", r.status_code)
print("Texto da resposta:\n")
print(r.text)