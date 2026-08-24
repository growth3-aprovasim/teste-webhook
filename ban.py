from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota que vai receber o POST do Sendflow
@app.route('/webhook', methods=['POST'])
def receber_alerta():
    # Captura os dados no formato JSON
    dados = request.json
    
    print("\n🚨 === NOVO ALERTA DO SENDFLOW === 🚨")
    print(dados) # Aqui você verá a estrutura que o Sendflow te envia
    print("======================================\n")
    
    # Retorna o status 200 para o Sendflow saber que você recebeu com sucesso
    return jsonify({"status": "recebido"}), 200

if __name__ == '__main__':
    # Roda o servidor local na porta 5000
    print("Aguardando webhooks na porta 5000...")
    app.run(host='0.0.0.0', port=5000)