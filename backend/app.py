from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from dataclasses import dataclass, asdict
import random
from datetime import datetime, timedelta
from flask import request, jsonify, abort

app = Flask(__name__)
CORS(app)
# Configuração do MongoDB
MONGO_URI = "mongodb://localhost:27017/"
client = MongoClient(MONGO_URI)
db = client['crime_analysis']
colecao = db['casos_criminais']

@dataclass
class Vitíma:
    etnia: str
    idade: int

@dataclass
calss Caso:
    data_do_caso: str
    tipo_do_caso: str
    vitima: Vitíma

    def to_dict(self):
        return{
            "data_do_caso": self.                 data_do_caso,
            "tipo_do_caso": self.tipo_do_caso,
            "localizacao": self.localizacao,
            "vitima": asdict(self.vitima)
        }

def gerar_casos_criminais(nu=20):
tipos_casos = ["Furto", "Assalto", "Violência doméstica", "Tráfico"]  
locais = ["Centro", "Bairro A", "Bairro B", "Zona Rural"]  
etnias = ["Branca", "Preto", "Parda", "Amarela", "Indígena"]
casos = []
base_date = datatime.now()
for i inn range(n):
    data_do_caso = (base_date - timedelta(days=random.randint(0, 365)).date().isoformat()
    caso = Caso(
        data_do_caso=data_do_caso,
        tipo_do_caso=random.choice(tipos_casos),
        localizacao=random.choice(locais),
        vitima=Vitíma(
            etnia=random.choice(etnias),
            idade=random.randint(1, 90)
        )
    )
    casos.append(caso.to_dict())
return casos
if __name__ == '__main__':
    if colecao.count_documents({}) == 0:
        print("Inserindo dados iniciais...")
        dados_iniciais = gerar_dados
        _aleatorios(20)
        colecao.insert_many(dados_iniciais)
    app.run(debug=True)




@app.route('/') 
def hello():
    return "Bem-vindo à API de análise de casos criminais"

def validar_caso_json(data):
    try:
        vitima = data['vitima']
        assert isinstance(vitima, dict)
        assert all(k in vitima for k in ('etnia', 'idade'))
        datatime.fromisoformat(data['data_do_caso'])
        assert isinstance(data['tipo_do_caso'], str)
        assert isinstance(data['localizacao'], str)
    execpt:
        return False
    return True

@app.route('/api/casos', methods=['GET'])
def listar_casos():
    documentos = list(colecao.find({}, {'_id': 0}))
    return jsonify(documentos), 200

@app.route('/api/casos', methods=['POST'])
def criar_caso():
    data = request.get_json()
    if not data or not validar_caso_json_caso_json(data):
        abort(400, "JSON inválido ou faltando campos obrigatórios")
    colecao.insert_one(data)
    return jsonify({"message": "Caso criado com sucesso"}), 201
        
    @app.route('/api/casos/<string:data_caso>', methods=['GET'])
    def obter_caso(data_caso):
        caso = colecao.find_one({'data_do_caso': data_caso}, {'_id': 0})
        if not caso:
            abort(404, "Caso não encontrado")
        return jsonify(caso), 200

    @app.route('/api/casos/<string:data_caso>', methods=['DELETE'])
    def deletar_caso(data_caso):
        resultado = colecao.delete_one({'data_do_caso': data_caso})
        if resultado.deleted_count == 0:
            abort(404, "Caso não encontrado")
        return jsonify({"message": "Caso deletado com sucesso"}), 200
    



if __name__ == '__main__':
    app.run(debug=True)