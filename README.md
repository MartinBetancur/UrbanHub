# UrbanHub

**UrbanHub** es una plataforma de ecommerce enfocada en la venta de sneakers, fragancias y hoodies de marcas prestigiosas como **Nike**, **Adidas**, **Chanel**, y **H&M**.

## Cómo ejecutar el proyecto

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

### 1. Clonar el repositorio

Primero, clona el repositorio en tu máquina local usando Git:

```bash
git clone https://github.com/usuario/urbanhub.git
cd urbanhub
```
### 2. Crear y activar el entorno virtual

Crea un entorno virtual para el proyecto y actívalo.

- En Linux/MacOS:

```bash
python -m venv venv
source venv/bin/activate
```
- En Windows:
```bash  
python -m venv venv
venv\Scripts\activate
```
### 3. Instalar las dependencias

Instala todas las dependencias necesarias usando el archivo `requirements.txt`:

```bash
pip install -r requirements.txt
```
### 4. Aplicar las migraciones de la base de datos

Ejecuta las migraciones para configurar la base de datos:

```bash
python manage.py migrate
```
### 5. Ejecutar el servidor de desarrollo

Para ejecutar el proyecto localmente, inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
```
Luego, abre tu navegador y accede a `http://127.0.0.1:8000/` para ver la aplicación en funcionamiento.
