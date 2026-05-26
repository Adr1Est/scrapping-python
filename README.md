# Python - Web Scrapping

Extrae nombre, precio y disponibilidad de productos de amazon y los guarda en csv.

- Versión de Python utilizada: 3.14.0a7

## Dependencias utilizadas

- os
- csv
- requests
- beautifulsoup4
- python-dotenv

## Instalación

```bash
# 1- Crear entorno virtual y activarlo
python -m venv venv
# En Windows (Bash)
source venv/Scripts/activate

# 2- Instalar las dependencias del proyecto
pip install -r requirements.txt

# Para salir del entorno virtual
deactivate
```

## Ejecutar

```bash
# 1. Crear archivo .env en la raiz del proyecto con las siguientes variables de entorno
ASINS=
GAME_PRODUCTS=

# 2. Escribir separados con "," y sin espacios los ASIN y CÓDIGOS de cada producto
ASINS=ASIN1,ASIN2,ASIN3,...
GAME_PRODUCTS=CODE1,CODE2,CODE3,...

python main.py
```
