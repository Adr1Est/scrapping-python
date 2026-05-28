# Python - Web Scraping

Proyecto para extraer **información** de productos de diferentes comercios y guardarla en un archivo `.csv`.

## Dependencias utilizadas

- os
- csv
- requests
- beautifulsoup4
- python-dotenv

> `os` y `csv` pertenecen a la librería estándar de Python, por lo que no requieren instalación.

## Instalación

### 1. Crear y activar el entorno virtual

```bash
python -m venv venv
```

**Windows (Bash)**

```bash
source venv/Scripts/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Salir del entorno virtual

```bash
deactivate
```

## Configuración

Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
ASINS=
GAME_PRODUCTS=
```

### Formato de las variables

Escribir los valores separados por comas (``,`), **sin espacios**.

```env
ASINS=ASIN1,ASIN2,ASIN3
GAME_PRODUCTS=CODE1,CODE2,CODE3
```

* `ASINS`: identificadores de productos de Amazon.
* `GAME_PRODUCTS`: códigos asociados a cada producto.

## Ejecución

Ejecutar el proyecto con:

```bash
python main.py
```
