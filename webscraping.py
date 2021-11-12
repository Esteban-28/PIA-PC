from bs4 import BeautifulSoup as bs
import requests
import re

def webscraping(url, x) :
    '''
    Hace webscraping para buscar emails o telefonos.

    Parametros:
        :url (str): URL deseada
        :x (str): La opcion a buscar
    Invocacion:
        -wb url x

    '''

    patt = r'[\(]?[\+]?(\d{2}|\d{3})[\)]?[\s]?((\d{6}|\d{8})|(\d{3}[\*\.\-\s]){3}|(\d{2}[\*\.\-\s]){4}|(\d{4}[\*\.\-\s]){2})|\d{8}|\d{10}|\d{12}'
    regex_email = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

    try:
        response = requests.get(url)
        if response.status_code == 200:

            soup = bs(response.text, "lxml")

            soupy = soup.get_text()

            if x == "tel":
                res = re.search(patt, soupy)
                if res != None:
                    print(res[0])
            elif x == "emails":
                res_em = re.search(regex_email, soupy)
                if res_em != None:
                    print(res_em[0])
                else:
                    print("No se encontraron resultados")

        else:
            print("No pudimos encontrar la URL")
    except:
        print("URL no encontrada o no valida")

