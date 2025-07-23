import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/rastrear", methods=["GET"])
def rastrear():
    cnpj = request.args.get("cnpj")
    nota = request.args.get("nota")

    if not cnpj or not nota:
        return jsonify({"erro": "CNPJ e nota são obrigatórios"}), 400

    url = "https://ssw.inf.br/2/rastreamento"
    payload = {
        "CNPJ": cnpj,
        "NotaFiscal": nota
    }
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    session = requests.Session()
    response = session.post(url, data=payload, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    resultados = []
    linhas = soup.select("table tr")
    for linha in linhas[1:]:
        colunas = linha.find_all("td")
        if len(colunas) >= 3:
            resultados.append({
                "data": colunas[0].text.strip(),
                "unidade": colunas[1].text.strip(),
                "situacao": colunas[2].text.strip()
            })

    return jsonify({"rastreamento": resultados})
