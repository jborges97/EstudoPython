import requests

def obter_clima(cidade, api_key):
    # URL da API do OpenWeatherMap com o nome da cidade e a chave da API
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang=pt_br&units=metric"
    
    # Faz a requisição para a API
    resposta = requests.get(url)
    
    # Verifica se a requisição foi bem-sucedida
    if resposta.status_code == 200:
        dados = resposta.json()
        
        # Extrai as informações relevantes
        temperatura = dados['main']['temp']
        descricao = dados['weather'][0]['description']
        umidade = dados['main']['humidity']
        vento = dados['wind']['speed']
        
        # Imprime as informações
        print(f"Clima em {cidade.capitalize()}:")
        print(f"Temperatura: {temperatura}°C")
        print(f"Descrição: {descricao.capitalize()}")
        print(f"Umidade: {umidade}%")
        print(f"Vento: {vento} m/s")
    else:
        print("Não foi possível obter as informações do clima para a cidade especificada.")

def main():
    cidade = input("Digite o nome da cidade: ")
    api_key = 'd63107f931b800dd431e199115d8209b'  # Substitua pela sua chave de API do OpenWeatherMap
    
    obter_clima(cidade, api_key)

if __name__ == "__main__":
    main()



