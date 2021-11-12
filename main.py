#Escrito en Python 3.9.2 por:
#Daniel Ernesto Rangel Perez
#Esteban Osorio Rodriguez

from funciones import *
from webscraping import webscraping
import argparse
import logging

logging.basicConfig(filename="logs.log", level=logging.info,
                    format='%(asctime)s:%(levelname)s:%(message)s')


if __name__ == "__main__":
    logging.info("***INICIO DE LA FUNCION MAIN***")
    description = '''Ejemplos de uso:
        [1] python main.py -es [si o no]
        [2] python main.py -ws [http://algun_url.algo] [emails o tel]
        [3] python main.py -ah [doc_existente.algo]
        [4] python main.py -au [http://algun_url.algo]
        [5] python main.py -af [doc_existente.algo]
        [6] python main.py -afh [Algun HASH obtenido]
        [7] python main.py -de [escribir algo]
    '''
    parser = argparse.ArgumentParser(description = 'PIA de PC',
                                    epilog = description,
                                    formatter_class = argparse.RawDescriptionHelpFormatter,
                                    exit_on_error= False
                                    )
    parser.add_argument("-es",
                        metavar="si",
                        dest="esc_red",
                        help="Detectara tu OS y escaneara tu red con Bash o PS"
                        )
        
    parser.add_argument("-ws",
                        nargs=2,
                        metavar=("https://www.uanl.mx/","emails"),
                        dest="wb_var",
                        help="Busca emails y telefonos en una pagina web.")

    parser.add_argument("-ah",
                        metavar="example.txt",
                        dest="na_fi",
                        help="Genera el SHA-256 de un archivo.")

    parser.add_argument("-au",
                        metavar="https://www.uanl.mx/",         
                       dest="ap_url",
                        help="Consulta a una API y te dice si el URL es seguro.")

    parser.add_argument("-af",
                        metavar="example.txt",
                        dest="ap_ar",
                        help="Consulta a una API y te dice si el archivo es seguro.")

    parser.add_argument("-afh",
                        metavar="20f5ede8bdd5284c4d218799d04a701a32e35ad2eeec7a7f07ac0ea55c36bafa",
                        dest="ap_fh",
                        help="Consulta a una API y te dice si el HASH es seguro.")

    parser.add_argument("-de",
                        metavar="example.txt",
                        dest="dec",
                        help="Desencripta un archivo con la misma llave enviada.")

    try:
        params, unknown = parser.parse_known_args()
    except Exception as err:
        print("Faltan argumentos.")
        logging.warning("Error por falta de argumentos")
        logging.info("***TERMINA FUNCION MAIN***")
    else:
        if params.wb_var != None:
            webscraping(params.wb_var[0], params.wb_var[1])
            logging.info("Se uso -wb")
            logging.info("***TERMINA FUNCION MAIN***")
        elif params.esc_red != None:
            net_os(params.esc_red)
            logging.info("Se uso -es")
            logging.info("***TERMINA FUNCION MAIN***")
        elif params.na_fi != None:
            obtHash(params.na_fi)
            logging.info("Se uso obtencion de -ah")
            logging.info("***TERMINA FUNCION MAIN***")
        elif params.ap_url != None:
            apiUrl(params.ap_url)
            logging.info("Se uso -au")
            logging.info("***TERMINA FUNCION MAIN***")
        elif params.ap_ar != None:
            apiArch(params.ap_ar)
            logging.info("Se uso -af")
            logging.info("***TERMINA FUNCION MAIN***")
        elif params.ap_fh != None:
            apiArchH(params.ap_fh)
            logging.info("Se uso -afh")
            logging.info("***TERMINA FUNCION MAIN***")
        elif params.dec != None:
            descifrado()
            logging.info("Se uso -de")
            logging.info("***TERMINA FUNCION MAIN***")
        else:
            print("Opcion no valida.\nUsa -h para mas informacion.")
            logging.warning("Error por opcion no valida")
            logging.info("***TERMINA FUNCION MAIN***") 
