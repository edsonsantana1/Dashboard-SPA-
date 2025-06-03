from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from dataclasses import dataclass, asdict
import random
from datetime import datetime, timedelta

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

if __name__ == '__main__':
    app.run(debug=True)