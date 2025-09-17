import requests
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os

# Faz a requisição para o Google
r = requests.get(
    'http://www.google.com/search',
    params={'q': 'elson de abreu'}
)

if r.status_code == 200:
    print("\nRequisição realizada com sucesso!")

    # 🔹 Defina o caminho completo do arquivo (altere conforme seu sistema)
    # Exemplo para Windows:
    caminho = r"C:/Users/Leonardo/documents\resultado_questão 5.pdf"
    # Exemplo para Linux/macOS:
    # caminho = "/home/seu_usuario/resultado_google.pdf"

    # Garante que a pasta existe
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    # Cria o PDF no local indicado
    doc = SimpleDocTemplate(caminho, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Resultado da busca no Google", styles["Title"]))
    story.append(Paragraph("Consulta: elson de abreu", styles["Heading2"]))
    story.append(Paragraph(r.text, styles["Normal"]))

    doc.build(story)

    print(f"Resultados salvos em: {caminho}\n")
else:
    print('Nao houve sucesso na requisicao.')