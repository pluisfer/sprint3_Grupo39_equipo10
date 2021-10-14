# README.MD

Documentación Proyecto Red social de Imágenes.

GRUPO 39

Equipo No. 10
Integrantes:
Luis Pacheco Acosta
Pablo Martínez Meza
Keylis Diaz Monsalve
Jose Minotta Ruiz

## Contenido

Este es un proyecto realizado en Flask , phyton, HTML, CSS y Js

## Rutas

/ ---> En donde esta iniciando el template registro-login.html
/seccion ---> Esta seccion aplicamos la logica en donde se redirecciona a la ruta iniciar
/iniciar ---> En esta seccion iniciamos el template index.html
/perfil ---> En esta seccion renderizamos el template perfil-usuario-portada.html
/perfil/seccion_perfil ---> En esta seccion renderizamos el template seccion-perfil-usuario.html
/dashboard ---> En esta seccion renderizamos el template dashboard.html

## logica

La logica aplicada fue en la ruta /seccion, en donde se realiza un acondicion para poder verificar usuario
y renderizar al template index.html.html

## Métodos

/ ---> sin metodo
/seccion ---> Metodo POST
/iniciar ---> Metodo GET y POST
/perfil ---> Metodo GET y POST
/perfil/seccion_perfil ---> Metodo GET y POST
/dashboard ---> Metodo GET y POST

## Instalacion

crear el entorno virtual

---

[ Inicio de entorno flask ]

[ 1 parte ]**********\_\_\_\_**********

python -m venv env <Inicar entorno>
´´´.\env\scripts\activate´´´ <Activar entono>
pip install flask <Instalar entorno>

[2 parte ]**********\_\_\_\_**********

Este el es codigo a instroducir en el archivo que se debe crear llamado app.py
´´´
from flask import Flask
app = Flask(_name_)

@app.route('/')
def hello():
return 'Hello World!'
´´´

[3 parte comandos para los <windows >]****\_\_\_\_****
(env) PS C:\Users\albertico\Desktop\API> env:FLASK_APP="app.py"
(env) PS C:\Users\albertico\Desktop\API> env:FLASK_ENV="development"
(env) PS C:\Users\albertico\Desktop\API> flask run
