import requests
from bs4 import BeautifulSoup
import csv

def main(hlavni_url, jmeno_souboru):
    if "https:" not in hlavni_url:
        print("Špatně zadané url")
        quit()
    elif ".csv" not in jmeno_souboru:
        print("Špatně zadaný název souboru")
        quit()
    else:
        sekundarni_url = ziskej_sekundarni_url(zpracuj_vsechny_obce(hlavni_url))
        kod_nazev = ['Kód obce', 'Název obce']
        cisla_obci = zpracuj_cisla_obci(zpracuj_vsechny_obce(hlavni_url))
        nazvy_obci = zpracuj_nazvy_obci(zpracuj_vsechny_obce(hlavni_url))
        strany_nadpisy = filtruj_nadpisy(zpracuj_informace_voleb(sekundarni_url[0])) + filtruj_strany(zpracuj_informace_voleb(sekundarni_url[0]))
        vysledny_zapis = kod_nazev + strany_nadpisy
        print("Zapisuji do souboru")
        zapis_csv(vysledny_zapis, jmeno_souboru)
        for index, url in enumerate(sekundarni_url):
            filtruj_nadpisy(zpracuj_informace_voleb(url))
            filtruj_pocet_volicu(zpracuj_informace_voleb(url))
            filtruj_strany(zpracuj_informace_voleb(url))
            filtruj_platne_hlasy_1(zpracuj_informace_voleb(url))
            filtruj_platne_hlasy_2(zpracuj_informace_voleb(url))
            hlasy_dohromady =  filtruj_pocet_volicu(zpracuj_informace_voleb(url)) + filtruj_platne_hlasy_1(zpracuj_informace_voleb(url)) + filtruj_platne_hlasy_2(zpracuj_informace_voleb(url))
            hlasy_dohromady.insert(0, nazvy_obci[index])
            hlasy_dohromady.insert(0, cisla_obci[index])
            zapis = hlasy_dohromady
            zapis_csv(zapis, jmeno_souboru)
        print("Data byla zapsána, ukončuji program")

# pro uvod
def zapis_csv(vysledny_zapis,jmeno_souboru):
    with open(jmeno_souboru, "a+", encoding="utf-8", newline='') as csv_vystup:
        zapisovani = csv.writer(csv_vystup)
        zapisovani.writerow(vysledny_zapis)

def zpracuj_vsechny_obce(hlavni_url):
    odpoved = requests.get(hlavni_url)
    soup = BeautifulSoup(odpoved.text, "html.parser")
    obce = soup.find("div", {"id": "publikace"})
    return obce

def zpracuj_cisla_obci(obce):
    cisla = obce.find_all("td", {"class": "cislo"}, "a")
    cisla_obci = []
    for obec in cisla:
        cisla_obci.append(obec.get_text(" "))
    return cisla_obci

def zpracuj_nazvy_obci(obce):
    nazvy = obce.find_all("td", {"class": "overflow_name"})
    nazvy_obci = []
    for nazev in nazvy:
        nazvy_obci.append(nazev.get_text(" "))
    return nazvy_obci

def ziskej_sekundarni_url(obce):
    url_jednotlivych_obci = obce.find_all("td", {"class": "cislo"})
    url_list = []
    for url in url_jednotlivych_obci:
        url_list.append(url.find("a")["href"])
    url2 = ["https://volby.cz/pls/ps2017nss/" + url_list[i] for i in range(len(url_list))]
    return url2

# pro for cyklus
def zpracuj_informace_voleb(url):
    odpoved = requests.get(url)
    soup = BeautifulSoup(odpoved.text, "html.parser")
    sekce = soup.find("div", {"id": "publikace"})
    return sekce


def filtruj_nadpisy(sekce):
    nadpisy_raw = sekce.find_all("th", {"data-rel": "L1"})
    filtrovane_nadpisy = []
    for prvek in nadpisy_raw:
        filtrovane_nadpisy.append(prvek.get_text(" "))
    return filtrovane_nadpisy

def filtruj_pocet_volicu(sekce):
    pocet_volicu_raw = sekce.find_all("td", {"data-rel": "L1"})
    filtrovane_pocty = []
    for cislo in pocet_volicu_raw:
        filtrovane_pocty.append(cislo.get_text(" "))
    filtrovane_pocty = [r.replace("\xa0", " ") for r in filtrovane_pocty]
    return filtrovane_pocty

def filtruj_strany(sekce):
    strany_raw = sekce.find_all("td", {"class": "overflow_name"})
    filtrovane_strany = []
    for strana in strany_raw:
        filtrovane_strany.append(strana.get_text(" "))
    return filtrovane_strany

def filtruj_platne_hlasy_1(sekce):
    platne_hlasy1_raw = sekce.find_all("td", {"headers": "t1sa2 t1sb3"})
    filtrovany_pocet_hlasu1 = []
    for cislo in platne_hlasy1_raw:
        filtrovany_pocet_hlasu1.append(cislo.get_text(" "))
    filtrovany_pocet_hlasu1 = [r.replace("\xa0", " ") for r in filtrovany_pocet_hlasu1]
    return filtrovany_pocet_hlasu1

def filtruj_platne_hlasy_2(sekce):
    platne_hlasy2_raw = sekce.find_all("td", {"headers": "t2sa2 t2sb3"})
    filtrovany_pocet_hlasu2 = []
    for cislo in platne_hlasy2_raw:
        filtrovany_pocet_hlasu2.append(cislo.get_text(" "))
    filtrovany_pocet_hlasu2 = [r.replace("\xa0", " ") for r in filtrovany_pocet_hlasu2]
    return filtrovany_pocet_hlasu2

if __name__ == '__main__':
    main(input("Zadej url: "), input("Zadej jméno souboru se zakončením .csv: "))
