from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def receber_alerta():
    dados = request.json
    
    # O flush=True força o texto a aparecer imediatamente no log
    print("\n🚨 === NOVO ALERTA DO SENDFLOW === 🚨", flush=True)
    print(dados, flush=True)
    print("======================================\n", flush=True)
    
    return jsonify({"status": "recebido"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)