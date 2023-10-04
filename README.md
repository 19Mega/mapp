# mapp

my_project/  
|-- app/  
|   |-- __init__.py  
|   |-- admin.py  
|   |-- app.py  
|   |-- models.py  
|   |-- utils.py  
|   |-- wsgi.py  
|-- venv/  
|-- .env  
|-- .gitignore  
|-- requirements.txt  

## Cómo ejecutar el proyecto: 

Para ejecutar tu proyecto Flask, debes asegurarte de que tu entorno virtual esté activado.   
Si aún no has creado un entorno virtual, puedes hacerlo utilizando el siguiente comando   
(asegúrate de estar en la carpeta principal de tu proyecto):  

python -m venv venv  

## Luego, activa el entorno virtual:  

En Windows:  
venv\Scripts\activate  
  
En macOS y Linux:  
source venv/bin/activate  

Después de activar el entorno virtual, puedes ejecutar tu aplicación Flask.  
Normalmente, en un proyecto Flask, ejecutarás el archivo wsgi.py para iniciar el servidor.  

## Puedes hacerlo de la siguiente manera:  
### Hay que entrar en app (cd app) y ejecutar 
python wsgi.py  

Tu aplicación Flask se ejecutará y estará disponible en la dirección   
local http://127.0.0.1:5000/. Puedes acceder a ella desde tu navegador web o   
realizar solicitudes HTTP a tus rutas.  



## **iniciar en una carpeta vacia**
$ git init (inicializa la carpeta como carpeta git)  
$ git remote add origin https://github.com/19Mega/mapp.git (agregamos repositorio remoto)  
$ git branch -m "main" (cambiamos nombre de rama actual)  
$ git pull origin main  (nos traemos los cambios de main)  

## **manejo branches**
$ git branch -b "ft-nueva-rama" (si se crea en github, hay que crearla en git-bash en windows)  
$ git checkout ft-cambiarse-rama  
$ git branch (muestra ramas)  


## base datos (no funciona)
flask db init  # Inicializa las migraciones (solo necesario la primera vez)
flask db migrate  # Crea las migraciones basadas en tus modelos
flask db upgrade  # Aplica las migraciones para crear las tablas en la base de datos

