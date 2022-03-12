# Popis projektu
Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Odkaz na prohlédnutí https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ
# Instalace knihoven
Všechny knihovny potřebné ke správnému spuštění kódu jsou uložené v souboru requirements.txt. Pro instalaci v PyCharmu klikněte na File -> settings -> Project:"name" -> Python Interpreter a pomocí pluska(install) nainstalujte potřebné knihovny, nebo pomocí nainstalovaného manažeru spustit: 
1. pip3 --version 
2. pip3 install -r requirements.txt
# Spuštení projektu
Spuštění projektu Scrapping Projekt 3.py po vás bude vyžadovat 2 argumenty. Do prvního zadáte url již vybrané obce pomocí X pod kolonkou "Výběr obce" ze stránek v popisu projektu a do druhého zadáte jméno souboru do kterého se vám následně uloží výsledky. Jméno souboru musí být zakončeno příponou ".csv"
# Ukázka projektu
Výsledky hlasování pro Prahu:
1. argument: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100  
2. argument: vysledky_praha.csv

Spuštění programu:

![argumenty](https://user-images.githubusercontent.com/95547788/158030337-da618779-7a57-46f0-968b-94f6c135bee4.PNG)

Průběh stahování:

![prubeh](https://user-images.githubusercontent.com/95547788/158030395-b50c5cd5-d0f3-4ae4-b4b4-8f6845d1fbfe.PNG)

Částečný výstup:

![castecnyvystup](https://user-images.githubusercontent.com/95547788/158030408-8834c62f-5190-40bd-9550-a37308a1b549.PNG)
