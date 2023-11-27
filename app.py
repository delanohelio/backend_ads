from flask import Flask, request, jsonify
from flask_cors import CORS
import random
from datetime import datetime
import project_terapias
from produto_SBJL import projetos, dados_do_formulario_lista
import project_smart_city

app = Flask(__name__)
CORS(app)
app.json.ensure_ascii = False


@app.route('/')
def OK():
    return 'OK'

############# Consulta Decisiva ################
@app.route('/consulta_decisiva', methods=['GET'])
def consulta_decisiva():
    data = {"total_de_vendas": random.randint(0, 200000),
            "lucro": random.randint(0, 50000),
            "distribuicao": random.randint(0, 20000),
            "clientes_atendidos": random.randint(0, 500),
            }
    return data

############# Future City ################
@app.route('/future_city', methods=['GET'])
def future_city():
    data = {"co2_mes": random.randint(0, 200000),
            "co2_evitado": random.randint(0, 50000),
            }
    return data

############# Eco Energy ################
@app.route('/eco_energy', methods=['GET'])
def eco_energy():
    data = {"kw_mes": random.randint(0, 500),
            "kw_atual": random.randint(0, 10),
            }
    return data

############# Projeto Terapias ################
@app.route('/terapia_depoimentos', methods=['GET'])
def get_terapia_depoimentos():
    return project_terapias.terapia_depoimentos

@app.route('/terapia_depoimentos', methods=['POST'])
def add_terapia_depoimento():
    try:
        depoimento = request.get_json()
        tipo_terapia = depoimento.get('tipo_terapia')
        if (tipo_terapia in project_terapias.terapia_depoimentos):
            depoimentos = project_terapias.terapia_depoimentos[tipo_terapia]
            depoimentos.append(
                {
                    "nome": depoimento.get("nome"),
                    "sobrenome": depoimento.get("sobrenome"),
                    "idade": depoimento.get("idade"),
                    "email": depoimento.get("email"),
                    "tratamento": depoimento.get("tratamento")
                }
            )
            return "Depoimento adicionado com sucesso"
        else:
            return jsonify({"error": "nao existe esse tipo de terapia"}), 400
    except Exception as e:
        print(f"Erro interno: {e}")
        return jsonify({"error": "Erro interno no servidor"}), 500

############# Smart City ################
@app.route('/smart_city', methods=['GET'])
def get_smart_city_depoimentos():
    return project_smart_city.projects_comments

@app.route('/smart_city', methods=['POST'])
def add_smart_city_depoimentos():
    try:
        depoimento = request.get_json()
        project = depoimento.get('project')
        if (project in project_smart_city.projects_comments):
            depoimentos = project_smart_city.projects_comments[project]
            depoimentos.append(
                {
                    "name": depoimento.get("name"),
                    "time": datetime.now(),
                    "text": depoimento.get("text")
                }
            )
            return "Depoimento adicionado com sucesso"
        else:
            return jsonify({"error": "nao existe esse projeto"}), 400
    except Exception as e:
        print(f"Erro interno: {e}")
        return jsonify({"error": "Erro interno no servidor"}), 500

############# Projeto SBJL ################
@app.route('/paginaProjeto/<index>', methods=['GET'])
def projeto(index):
    return projetos[int(index)]

@app.route('/adicionar_comentario', methods=['POST'])
def adicionar_comentario():
    try:
        if request.is_json:
            data = request.get_json()

            numero = data.get('numero')
            if numero is None:
                return jsonify({"error": "O campo 'numero' é obrigatório"}), 400
            else:
                numero = int(numero)
    
            comentario = {
                "nome": data.get('nome'),
                "comentario": data.get('comentario')
            }

            if (numero >= 0 and numero < len(projetos)):
                projeto = projetos[numero]
                projeto["comentarios"].append(comentario)
            else:
                return jsonify({"error": "o numero nao esta dentro da lista de projetos"}), 400

            return jsonify({"message": "Comentário recebido e salvo com sucesso"}), 200
        else:
            return jsonify({"error": "A solicitação deve conter dados JSON"}), 400
    except Exception as e:
        print(f"Erro interno: {e}")
        return jsonify({"error": "Erro interno no servidor"}), 500

@app.route('/enviarFormulario', methods=['POST'])
def enviarFormulario():
    try:
        dados_do_formulario = request.get_json()
        dados_do_formulario_lista.append(dados_do_formulario)

        print("Lista de dados do formulário:")
        print(dados_do_formulario_lista)

        return jsonify({"message": "Dados do formulário recebidos com sucesso!"}), 200

    except Exception as e:
        print(f"Erro interno: {e}")
        return jsonify({"error": "Erro interno no servidor"}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0')
