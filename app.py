from flask import Flask
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def OK():
    return 'OK'

#total de vendas
#lucro
#distribuição
#clientes atendidos
@app.route('/consulta_decisiva', methods=['GET'])
def consulta_decisiva():
    data = {"total_de_vendas": random.randint(0, 200000),
            "lucro": random.randint(0, 50000),
            "distribuicao": random.randint(0, 20000),
            "clientes_atendidos": random.randint(0, 500),
            }
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0')
