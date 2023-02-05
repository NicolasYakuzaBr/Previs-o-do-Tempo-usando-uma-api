import requests
import datetime as dt


while True:
    
    api_key = "5ce8b7b2eec71bfa55b94eaa21618308"
    city_name = input('Insira uma cidade ou "CTRL + C" para sair: ')
    lang = 'pt_br'
    link = (f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric&lang={lang}")

    
    requisição = requests.get(link).json()


    temperatura = requisição['main']['temp']
    sensação = requisição['main']['feels_like']
    umidade = requisição['main']['humidity']
    descrição = requisição['weather'][0]['description']
    nascer_sol = dt.datetime.utcfromtimestamp(requisição['sys']['sunrise'] + requisição['timezone'])
    por_sol = dt.datetime.utcfromtimestamp(requisição['sys']['sunset'] + requisição['timezone'])
    vel_vento = str(int(requisição['wind']['speed'])*3.6) + 'km/h'
    temp_min = requisição['main']['temp_min']
    temp_max = requisição['main']['temp_max']
    print('----------------------------------------')

    print(f"Temperatura atual é: {temperatura}°C")
    print(f"Sensação térmica de: {sensação}°C")
    print(f"Umidade atual é: {umidade}%")
    print(f"Velocidade do vento é:  {vel_vento}")
    print(f"Previsão atual: {descrição}")
    print(f"Nascer do sol ás: {nascer_sol}")
    print(f"Por do sol ás: {por_sol}")
    print(f"Temperatura Mínima: {temp_min}")
    print(f"Temperatura Máxima: {temp_max}")

    print('----------------------------------------')

    
    
        

        

 



    


     

   










