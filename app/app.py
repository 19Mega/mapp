from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Vehicle, Planet, Favourite
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

app = Flask(__name__)
app.url_map.strict_slashes = False

# Configuración de la aplicación Flask aquí


# Definición de endpoints de prueba
@app.route('/')
def hello_world():
    return jsonify(message='¡Hola, mundo!')

@app.route('/saludo/<nombre>')
def saludo_personalizado(nombre):
    return jsonify(message=f'Hola, {nombre}!')



@app.route('/signup', methods=['POST'])
def signup():
    request_body = request.get_json(force=True)
     
    new_user = User(username=request_body["username"],
                    email = request_body["email"], 
                    password = request_body["password"],
                    is_active = request_body["is_active"]
                    )

    db.session.add(new_user)
    db.session.commit()
   
    return { "msg": "Usuario creado con éxito",
            "response": new_user.serialize(),
            }