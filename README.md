# mapp
Backend

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

Cómo ejecutar el proyecto:

Para ejecutar tu proyecto Flask, debes asegurarte de que tu entorno virtual esté activado. 
Si aún no has creado un entorno virtual, puedes hacerlo utilizando el siguiente comando 
(asegúrate de estar en la carpeta principal de tu proyecto):

python -m venv venv
Luego, activa el entorno virtual:

En Windows:
Copy code
venv\Scripts\activate
En macOS y Linux:

bash linux:
source venv/bin/activate
Después de activar el entorno virtual, puedes ejecutar tu aplicación Flask. 
Normalmente, en un proyecto Flask, ejecutarás el archivo wsgi.py para iniciar el servidor. 
Puedes hacerlo de la siguiente manera:

python wsgi.py
Tu aplicación Flask se ejecutará y estará disponible en la dirección 
local http://127.0.0.1:5000/. Puedes acceder a ella desde tu navegador web o 
realizar solicitudes HTTP a tus rutas.

