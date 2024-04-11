import pyautogui
from RequestTextos import obter_texto_da_api

pyautogui.FAILSAFE = True
pyautogui.click(100, 100)   

def EscreverTexto(texto):
    try:
        while True:
            pyautogui.typewrite(texto, interval=0.001)
    except pyautogui.FailSafeException:
        print("FailSafe ativo")
    
url_da_api = "http://servicodados.ibge.gov.br/api/v3/noticias/?de=04/10/2024"

texto_da_api = obter_texto_da_api(url_da_api, tempo_minimo=5)

if texto_da_api:
    EscreverTexto(texto_da_api)
else:
    print("Não foi possível obter o texto da API.") 