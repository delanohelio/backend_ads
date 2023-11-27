from flask import Flask, request, jsonify
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route('/')
def OK():
    return 'OK'


comentarios_listCitySewer = []
comentarios_listWaterResponsible = []
comentarios_listSolidWaste = []

@app.route('/City-Sewer', methods=['GET'])
def City_Sewer():
    data = {
        "title":'Tratamento de Esgoto da Cidade',
        "introduction": "No cenário contemporâneo, a gestão eficiente dos recursos naturais tornou-se imperativa para o desenvolvimento sustentável das comunidades. Nesse contexto, o Projeto de Tratamento de Esgoto da Cidade emerge como uma iniciativa visionária que não apenas aborda as crescentes preocupações ambientais, mas também promove uma transformação significativa na qualidade de vida dos habitantes locais. Ao implementar um sistema de tratamento de esgoto inovador, este projeto representa um marco crucial na busca por soluções ambientais e destaca-se como um exemplo inspirador de como a engenhosidade humana pode ser canalizada para promover a harmonia entre a urbanização e a preservação do meio ambiente.",
        "paragraph1": "O sistema de tratamento de esgoto de última geração adotado no projeto revela-se uma resposta eficaz às preocupações cada vez mais prementes relacionadas à poluição dos rios e à qualidade da água na cidade. Ao longo de um período de dedicada pesquisa e desenvolvimento, a equipe responsável conseguiu conceber e implementar um sistema que não apenas reduziu de forma significativa a poluição dos rios locais, mas também promoveu uma melhoria notável na qualidade da água. Esse avanço não só beneficiou a vida aquática, proporcionando ecossistemas mais saudáveis, mas também assegurou água potável de alta qualidade para o consumo humano. A dedicação incansável da equipe em tornar esse projeto uma realidade reflete-se nos resultados tangíveis que agora contribuem para a prosperidade e sustentabilidade da comunidade.",
        "paragraph2": "Além disso, o Projeto de Tratamento de Esgoto da Cidade não se limita a mitigar os impactos ambientais negativos; ele atua como um agente catalisador para o desenvolvimento sustentável. A implementação bem-sucedida do sistema não apenas elevou a qualidade de vida dos residentes, proporcionando um ambiente mais limpo e saudável, mas também abriu caminho para a construção de uma comunidade mais consciente e proativa em relação à preservação ambiental. Este projeto não apenas representa uma realização técnica, mas também um modelo inspirador para outras localidades enfrentando desafios semelhantes, reforçando a ideia de que investir em soluções ecologicamente sustentáveis é vital para o progresso a longo prazo.",
        "conclusion": "Em suma, o Projeto de Tratamento de Esgoto da Cidade é um exemplo eloquente de como a inovação e o comprometimento podem convergir para resolver desafios ambientais complexos. Ao transformar a maneira como a cidade lida com o esgoto, não apenas mitigamos os danos causados à natureza, mas também pavimentamos o caminho para uma comunidade mais resiliente e voltada para o futuro. Os benefícios tangíveis desse projeto não só ressoam nos rios agora mais limpos, mas ecoam na qualidade de vida aprimorada, na promoção da sustentabilidade e no legado de uma cidade que escolheu cuidar de seu meio ambiente para as gerações futuras.",
        "comentario": comentarios_listCitySewer,
        }
    return data

@app.route('/Water-Responsible', methods=['GET'])
def Water_Responsible():
    data = {
        "title": "Uso Responsável da Água",
        "introduction": "A Campanha de Conscientização sobre o Uso Responsável da Água surge como uma resposta proativa a uma das questões mais cruciais da contemporaneidade: a gestão sustentável dos recursos hídricos. Em consonância com a crença de nossa empresa de que a conscientização é o ponto de partida para transformações positivas, essa iniciativa foi concebida com o propósito de educar e engajar a comunidade na preservação responsável da água. Ao longo da campanha, uma série de eventos educacionais, workshops e iniciativas de sensibilização pública foram realizados, todos com o objetivo de destacar a importância da água e fomentar práticas conscientes de uso. A comunidade respondeu de maneira extraordinária, evidenciando uma redução notável no desperdício de água e uma crescente conscientização acerca da necessidade premente de proteger esse recurso vital para as gerações futuras.",
        "paragraph1": "No âmago da campanha, a realização de eventos educacionais proporcionou uma plataforma dinâmica para disseminar conhecimento sobre a importância da água e os impactos do uso irresponsável. Workshops especializados abordaram estratégias práticas para a conservação hídrica, capacitando os participantes a adotarem medidas sustentáveis em suas rotinas diárias. Além disso, iniciativas de sensibilização pública, como campanhas em redes sociais e eventos comunitários, amplificaram a mensagem, gerando uma conscientização abrangente. A notável resposta da comunidade não apenas se refletiu em estatísticas tangíveis de redução no desperdício de água, mas também criou uma cultura local mais atenta à necessidade premente de proteger esse recurso vital. Este projeto exemplifica a eficácia da educação aliada à ação coletiva na promoção de mudanças de comportamento e na construção de um futuro mais sustentável.",
        "paragraph2": "Em síntese, a Campanha de Conscientização sobre o Uso Responsável da Água não apenas atingiu seus objetivos educativos e de sensibilização, mas também moldou positivamente a mentalidade e as práticas da comunidade em relação ao precioso recurso hídrico. A redução significativa no desperdício de água é testemunho claro do impacto direto desta iniciativa. Este projeto não apenas reforça a convicção de que a educação é um catalisador poderoso para a mudança, mas também estabelece um precedente inspirador para outras comunidades, indicando que a união de esforços pode transformar desafios complexos em oportunidades tangíveis para um futuro mais sustentável e equitativo.",
        "conclusion": "Em suma, a Campanha de Conscientização sobre o Uso Responsável da Água representa não apenas um esforço educativo, mas uma jornada coletiva em direção à preservação de nosso recurso mais precioso. Os números refletem uma mudança real no comportamento da comunidade, destacando a eficácia de abordagens inclusivas e educativas. À medida que celebramos a redução no desperdício de água e o aumento da conscientização, também reconhecemos que essa campanha é mais do que um projeto isolado; é um passo significativo em direção a um futuro onde a gestão responsável da água é uma prioridade compartilhada. Este é um legado que transcende os números, influenciando a forma como vivemos e preservamos nosso meio ambiente para as gerações que virão." ,
        "comentario": comentarios_listWaterResponsible,
    }
    return data


@app.route('/Solid-Waste', methods=['GET'])
def Solid_Waste():
    data = {
        "title": "Coleta Seletiva de Resíduos Sólidos",
        "introduction": "No contexto atual, o aumento exponencial da produção de resíduos sólidos representa um desafio ambiental significativo. Em resposta a essa urgência, nosso projeto de Coleta Seletiva de Resíduos Sólidos surge como uma iniciativa proativa e eficaz para abordar a questão premente dos resíduos, visando não apenas a redução do impacto ambiental, mas também a promoção de uma gestão mais consciente e sustentável dos recursos. Ao implementar um programa abrangente de coleta seletiva, focado na separação de materiais recicláveis e resíduos orgânicos, buscamos ativamente transformar a maneira como encaramos e lidamos com o ciclo de vida dos materiais descartados.",
        "paragraph1": "No âmago do nosso projeto, a implementação da coleta seletiva não se limitou apenas à segregação de resíduos; ela representou um compromisso mais amplo com a comunidade. Trabalhamos em estreita colaboração com os residentes, promovendo a conscientização sobre a importância da reciclagem e reutilização de materiais. Eventos educacionais, campanhas de sensibilização e parcerias com escolas foram instrumentais para estimular práticas mais sustentáveis no cotidiano das pessoas. A resposta positiva foi palpável, refletindo não apenas em números estatísticos, como na expressiva redução na quantidade de resíduos destinados a aterros sanitários, mas também na construção de uma mentalidade comunitária voltada para a preservação ambiental. Este projeto não apenas se configura como um catalisador para a gestão eficaz de resíduos em nossa comunidade, mas também se destaca como um modelo inspirador de como pequenas mudanças no nível local podem ter repercussões globais, contribuindo para um planeta mais equilibrado e sustentável.",
        "paragraph2": "Em síntese, a Coleta Seletiva de Resíduos Sólidos transcende seu propósito inicial de lidar com a problemática local dos resíduos sólidos. Ao evidenciar a viabilidade e os benefícios tangíveis de práticas mais sustentáveis, este projeto representa um testemunho vivo de como a ação local pode gerar impactos globais. A redução significativa na quantidade de resíduos enviados para aterros sanitários é mais do que uma métrica; é um indicativo de uma mudança de paradigma em direção a uma cidade mais limpa, eficiente e ambientalmente responsável. Esta iniciativa não apenas responde ao desafio dos resíduos sólidos, mas também sinaliza um compromisso duradouro com a construção de comunidades que reconhecem a interconexão entre a saúde do meio ambiente e a qualidade de vida dos seus habitantes.",
        "conclusion": "Em suma, a Coleta Seletiva de Resíduos Sólidos transcende seu impacto local, representando um passo significativo em direção a práticas mais sustentáveis e conscientes. Ao mitigar os efeitos negativos da produção excessiva de resíduos, este projeto não apenas contribui para a conservação ambiental, mas também inspira comunidades a repensarem seus hábitos e adotarem medidas concretas para um futuro mais sustentável. Os resultados tangíveis e a transformação cultural que acompanham essa iniciativa solidificam a convicção de que, por meio de ações coletivas, podemos moldar um mundo onde a gestão responsável dos resíduos é intrínseca à maneira como vivemos e preservamos nosso planeta para as gerações vindouras.",
        "comentario": comentarios_listSolidWaste,
    }
    return data


    


# ... Seu código existente ...

@app.route('/adicionar_comentario', methods=['POST'])
def adicionar_comentario():
    try:
        if request.is_json:
            data = request.get_json()
            
            numero = data.get('numero')
            if numero is None:
                return jsonify({"error": "O campo 'numero' é obrigatório"}), 400

            comentario = {
                "nome": data.get('nome'),
                "comentario": data.get('comentario')
            }

            if numero == '1':
                comentarios_listCitySewer.append(comentario)
            elif numero == '2':
                comentarios_listWaterResponsible.append(comentario)
            elif numero == '3':
                comentarios_listSolidWaste.append(comentario)
            else:
                return jsonify({"error": "O campo 'numero' deve ser 1, 2 ou 3"}), 400

            return jsonify({"message": "Comentário recebido e salvo com sucesso"}), 200
        else:
            return jsonify({"error": "A solicitação deve conter dados JSON"}), 400
    except Exception as e:
        print(f"Erro interno: {e}")
        return jsonify({"error": "Erro interno no servidor"}), 500


dados_do_formulario_lista=[]

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