# PIA-PC
Herramientas englobadas en un solo script para ciberseguridad

## Presentacion
Este script esta pensado para agilizar las tareas de ciberseguridad que nos pueden servir para algun analisis de riesgo, asi como, tiene la intencion de aplicar lo aprendido en las clases de Programacion para Ciberseguridad, contiene:
```
        Analisis de subredes

        Obtencion de hashes

        Envio de correos electronicos

        Etc.
```

## Instalacion
La instalacion solo requiere de instalar el archivo requirements.txt:
```
pip install -r requirements.txt
```
Via git:
```
git clone https://github.com/Esteban-28/PIA-PC
pip install -r requirements.txt
```
Via GitHub:
```
-https://github.com/Esteban-28/PIA-PC
```

## Aclaraciones
Todos los archivos utilizados deben estar en la misma carpeta, es decir, los modulos, archivos a evaluar, llave de encriptacion, etc. Deben estar juntos para su optimo funcionamiento.
### Para reporte de errores contactar a:
- esteban.osorior@uanl.edu.mx
- ernesto.rangelprz@uanl.edu.mx

## Ejemplos de uso
- python main.py -es si
- python main.py -ws https://www.uanl.mx/ tel
- python main.py -ah example.txt
- python main.py -au https://www.uanl.mx/
- python main.py -af example.txt
- python main.py -afh 20f5ede8bdd5284c4d218799d04a701a32e35ad2eeec7a7f07ac0ea55c36bafa
- python main.py -de a

## Autores
-Esteban Osorio Rodriguez
-Daniel Ernesto Rangel Perez

## Licencia
GPL-3.0 License 
https://github.com/Esteban-28/PIA-PC/blob/main/LICENSE

# PIA
## funciones module

### funciones.apiArch(api_file)
   Analiza archivos propios y determina si son seguros.
    Parametros:
        api_file (str):       Archivo que se desea Analizar.
    Invocacion:
        -af api_file

### funciones.apiArchH(hash)
   Analiza un HASH para determinar si es seguro.
    Parametros:
        hash (str):     HASH que se desea Analizar
    Invocacion:
        -afh hash

### funciones.apiUrl(ind)
   Analiza si una URL es segura.
    Parametros:
        ind (str):      URL que se desea Analizar
        
   Invocacion:
        -au ind

### funciones.cifrado()
   Cifra el archivo generado en otra funcion.
    Parametros:         No necesita parametros.
    
   Invocacion:
        Se ejecuta por si solo, no por separado.

### funciones.descifrado()
   Cifra el archivo generado en otra funcion.
    Parametros:         No necesita parametros.
    
   Invocacion:
        Se ejecuta por si solo, no por separado.

### funciones.email()
   Envio de emails.
    Parametros:         No necesita parametros.
    
   Invocacion:
        Se ejecuta por si solo, no por separado.

### funciones.net_os(rex)
   Detecta el OS en que se esta trabajando y escanea las subredes.
    Parameters:
        rex (str):      Opcion seleccionada

### funciones.obtHash(inFile)
   Genera el SHA-256 de un archivo.
    Parametros:
        inFile (str):   Archivo de que se desea generar el HASH
        
   Invocacion:
        -af inFile


# webscraping module

### webscraping.webscraping(url, x)
   Hace webscraping para buscar emails o telefonos.
    Parametros:
        url (str):      URL deseada
        x (str):        La opcion a buscar
        
   Invocacion:
        -wb url x


