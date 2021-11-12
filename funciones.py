#Escrito en Python 3.9.2 por:
#Daniel Ernesto Rangel Perez
#Esteban Osorio Rodriguez

import requests
import json
import hashlib
import platform
import subprocess
import getpass
import yagmail
from cryptography.fernet import Fernet
import logging

logging.basicConfig(filename="logs.log", level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

api_key = "c718bf3831360637fa949f7df711c6763f1dc3d5ce318fbf9f894377aab43a95"

#Deteccion de sistema operativo
my_os = platform.system()

def cifrado():
    '''
    Cifra el archivo generado en otra funcion.
    
    Parametros:
        No necesita parametros.

    Invocacion:
        Se ejecuta por si solo, no por separado.
    '''

    logging.info("***COMIENZO DE CIFRADO***")
    clave = Fernet.generate_key()
    archivo_key = open ('clave.key', 'wb')
    archivo_key.write(clave)
    logging.info("Se creo el archivo clave.key")

    with open('clave.key', 'rb') as filekey: 
        key = filekey.read() 
        fernet = Fernet(clave) 

    with open('escaneo.txt', 'rb') as file: 
        original = file.read() 
        encrypted = fernet.encrypt(original) 
        logging.info("Se encripto el archivo escaneo.txt")

    with open('escaneo_c.txt', 'wb') as encrypted_file: 
        encrypted_file.write(encrypted)
        logging.info("Se creo el archivo escaneo_c.txt")
    
    logging.info("***FINALIZA CIFRADO**")

def descifrado():
    '''
    Cifra el archivo generado en otra funcion.
    
    Parametros:
        No necesita parametros.

    Invocacion:
        Se ejecuta por si solo, no por separado.
    '''
    logging.info("***COMIENZO DE DESCIFRADO***")
    try:
        with open("clave.key","rb") as file:
            var = file.read()
            key = Fernet(var)

        with open("escaneo_c.txt", 'rb') as enc_file: 
            encrypted = enc_file.read() 
            decrypted = key.decrypt(encrypted)
            logging.info("Se desencripto el archivo escaneo_c.txt")
    except FileNotFoundError:
        print("No se encontraron los archivos.")
        logging.warning("No se encontraron los archivos")
    else:
        with open('escaneo_d.txt', 'wb') as dec_file: 
            dec_file.write(decrypted)
            print("Se genero ecaneo_d.txt")
            logging.info("Se creo el archivo escaneo_d.txt")
    logging.info("***FINALIZA DESCIFRADO***")


#Envio de correo.
def email():
    '''
    Envio de emails.
    
    Parametros:
        No necesita parametros.

    Invocacion:
        Se ejecuta por si solo, no por separado.
    '''

    logging.info("***INICIA EMAIL***")
    subject = "infoRME SCRIPT PIA"
    body = ['escaneo_c.txt', 'clave.key']
    sender_email = input("Correro del Emisor: ")
    receiver_email = input("Correo del Receptor: ")
    password = getpass.getpass()
    logging.info("Se completo el formulario necesario")
    try:
        yag = yagmail.SMTP(sender_email,password)

        yag.send(receiver_email, subject, body)
    except:
        print("Correo no valido o contraseña no valida")
        logging.warning("Error en la validacion de usuario.")
        logging.info("***TERMINA EMAIL***")
    else:
        logging.info("Acceso a correo exitoso.")
        logging.info("***TERMINA EMAIL***")

#En caso de que sea LINUX
def net_os(rex):
    '''
    Detecta el OS en que se esta trabajando y escanea las subredes.
    
    Parameters:
        :rex (str): Opcion seleccionada
    '''
    logging.info("***INICIA ESCANEO***")
    print("Tu sistema operativo es: " + my_os) 
    logging.info("El SO en el que se esta trabajando es:" + my_os)
    if my_os != "Windows":
        print("Escaneando subredes...")
        asd = subprocess.run(["./netscan"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        foo = asd.stdout.decode()
        with open("escaneo.txt", "w") as file:
            file.write(foo)
        logging.info("Se creo el archivo escaneo.txt")
        print("Se creo escaneo.txt")
        logging.info("***TERMINA ESCANEO***")

        if rex == "si":
            cifrado()
            logging.info("Se manda a cifrar el archivo")
            email()
            logging.info("Se envia por email.")
        logging.info("***TERMINA ESCANEO***")
    else:
        print("El proceso podria tardar varios minutos...")
        foo = subprocess.run(["powershell.exe", ".\\escaneoPS.ps1"], stdout=subprocess.PIPE)
        res = foo.stdout.decode()
        with open("escaneo.txt", "w") as file:
            file.write(res)
        print(res)
        logging.info("Se creo el archivo escaneo.txt")
        logging.info("***TERMINA ESCANEO***")
        if rex == "si":
            cifrado()
            logging.info("Se manda a cifrar el archivo")
            email()
            logging.info("Se envia por email.") 
        logging.info("***TERMINA ESCANEO***")

#Obtencion de HASHES
def obtHash(inFile):
    '''
    Genera el SHA-256 de un archivo.
    
    Parametros:
        :inFile (str): Archivo de que se desea generar el HASH

    Invocacion:
        -af inFile
    '''
    logging.info("***INICIO OBTENCION DE HASHES***")
    global mh

    try:
        opFile = open(inFile, "rb")
        reFile = opFile.read()
        m = hashlib.sha256(reFile)
        mh = m.hexdigest()
        logging.info("Se genera el SHA-256" + mh)

        print("File Name: %s" % inFile)
        print("SHA256: %r" % mh)
        logging.info("***TERMINA OBTENCION DE HASHES***")
    except FileNotFoundError:
        print("El archivo no existe o no es valido.")
        logging.warning("No se encontraron archivos")
        logging.info("***TERMINA OBTENCION DE HASHES***")

#API de URLs
def apiUrl(ind):
    '''
    Analiza si una URL es segura.

    Parametros:
        :ind (str): URL que se desea Analizar

    Invocacion:
        -au ind
    '''
    logging.info("***INICIO DE API URL***")
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    #"https://tailstory.top/MercadoLibre/tb.php?_t=1623792509"
    try:
        params = {'apikey': api_key, 'resource': ind}
        count = 0

        r = requests.get(url, params=params)
        r_json = json.loads(r.content)
        logging.info("Consulta a la API")


        if r_json['response_code'] == 0:
            print("No se encontro la URL")
            logging.info("No se encontro la URL")
            logging.info("***TERMINA API URL***")
        else:
            for i in r_json['scans']:
                if r_json['scans'][i]['detected'] == True:
                    print(i + " detecto anomalias en esta URL")
                    logging.info(i + " detecto anomalias en esta URL")
                    count = count + 1

            if count == 0:
                print("URL segura")
                logging.info("URL segura")

            logging.info("***TERMINA API URL***")
    except:
        print("Error de conexion")
        logging.warning("ERROR DE CONEXION")
        logging.info("***TERMINA API URL***")

# Analisis de archivos
def apiArch(api_file):
    '''
    Analiza archivos propios y determina si son seguros.

    Parametros:
        :api_file (str): Archivo que se desea Analizar.

    Invocacion:
        -af api_file
    '''

    logging.info("***INICIA API ARCHIVOS***")
    url1 = 'https://www.virustotal.com/vtapi/v2/file/report'

    obtHash(api_file)
    try:
        try:
            params = {'apikey': api_key, 'resource':  mh}

            response = requests.get(url1, params=params)

            res_json = json.loads(response.content)
            logging.info("Consulta a la API")

            if res_json['response_code'] == 0:
                print("Archivo no valido")
                logging.info("Archivo no valido")
                logging.info("***TERMINA API ARCHIVOS***")
            else:
                if res_json['positives'] == 0:
                    print("Archivo seguro")
                    logging.info("Archivo seguro")
                    logging.info("***TERMINA API ARCHIVOS***")
                else:
                    for i in res_json['scans']:
                        if res_json['scans'][i]['detected'] == True:
                            print(i + ' detecto anomalias')
                            logging.info(i + ' detecto anomalias')
                            logging.info("***TERMINA API ARCHIVOS***")
        except:
            print("Error de conexion")
            logging.warning("ERROR DE CONEXION")
    except NameError:
        print("No se genero el SHA-256")
        logging.warning("Fallo en la generacion de SHA-256")
        logging.info("***TERMINA API ARCHIVOS***")

# Analisis de archivos por Hash
def apiArchH(hash):
    '''
    Analiza un HASH para determinar si es seguro.

    Parametros:
        :hash (str): HASH que se desea Analizar

    Invocacion:
        -afh hash
    '''

    logging.info("***INICIO DE API HASH***")
    url1 = 'https://www.virustotal.com/vtapi/v2/file/report'

    params = {'apikey': api_key, 'resource':  hash}

    try:
        response = requests.get(url1, params=params)
        res_json = json.loads(response.content)
        logging.info("Se consulta a a la API")

        if res_json["response_code"]==0:
            print("HASH no valido")
            logging.info("HASH no valida")
        else:
            if res_json['positives'] == 0:
                print("HASH seguro")
                logging.info("HASH seguro")
                logging.info("***TERMINA API HASH***")
            else:
                for i in res_json['scans']:
                    if res_json['scans'][i]['detected'] == True:
                        print(i + ' detecto anomalias')
                        logging.info(i + ' detecto anomalias')
                        logging.info("***TERMINA API HASH***")
    except:
        print("Ha ocurrido un error de conexion.")
        logging.warning("ERROR DE CONEXION")
