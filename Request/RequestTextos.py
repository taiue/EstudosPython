import requests

def obter_texto_da_api(url, tempo_minimo=5):
    try:
        response = requests.get(url, timeout=(tempo_minimo, None))
        
        if response.status_code == 200:
            return response.text
        else:
            print("Erro ao fazer requisição à API:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Erro ao fazer requisição à API:", e)
        return None
