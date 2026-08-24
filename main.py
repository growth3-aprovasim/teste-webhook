import requests
import json

BASE_URL = "https://sendapi.sendflow.pro"
API_KEY = "send_api-jvuah84s0z1dhu4mx3tbiobk6kt0shztzwdi8cql" # Substitua pela sua chave real

def fetch_accounts():
    print("Iniciando requisição para GET /accounts...\n")
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(f"{BASE_URL}/accounts", headers=headers)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("Sucesso! Contas obtidas:\n")
            
            # Percorre a lista e imprime apenas os campos desejados
            for conta in data:
                nome = conta.get("name")
                numero = conta.get("jidPrefix")
                status = conta.get("status")
                
                print(f"Nome: {nome} | Número: {numero} | Status: {status}")
            
        elif response.status_code == 401:
            print("Erro 401: Falha de autenticação. Verifique sua API Key.")
            
        elif response.status_code == 403:
            print("Erro 403: Limite de operações atingido (Rate Limit) ou acesso negado.")
            print("Lembrete: Aguarde pelo menos 60 segundos antes de tentar novamente.")
            
        elif response.status_code == 400:
            print("Erro 400: Erro na requisição ao obter contas.")
            
        else:
            print(f"Erro Inesperado ({response.status_code}):", response.text)
            
    except requests.exceptions.RequestException as e:
        print("Erro de conexão ou execução:", e)

if __name__ == "__main__":
    fetch_accounts()