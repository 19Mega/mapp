from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Vehicle, Planet, Favourite
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

# Flask app
app = Flask(__name__)
app.url_map.strict_slashes = False # slash at the end of the url

# Data Base Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Cambia esto al URI de tu base de datos
db.init_app(app)
migrate = Migrate(app, db)

# Función para crear o migrar las tablas en la base de datos
def create_or_migrate_db():
    with app.app_context():
        db.create_all()

# Definición de endpoints de prueba
@app.route('/')
def hello_world():
    return jsonify(message='¡Hola, mundo!')



@app.route('/signup', methods=['POST'])
def signup():
    request_body = request.get_json(force=True)
    print(request_body)
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



if __name__ == "__main__":
    generate_sitemap()  # Genera el sitemap cuando se ejecuta el servidor
    create_or_migrate_db()  # Crea o migra la base de datos al ejecutar el servidor
