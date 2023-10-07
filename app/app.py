from flask import Flask, request, jsonify, url_for, Blueprint, render_template_string
from flask_migrate import Migrate
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
import json
from models import db, User
#from models import db, User, People, Vehicle, Planet, Favourite
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager
from flask_bcrypt import Bcrypt


# Flask app
app = Flask(__name__)
app.url_map.strict_slashes = False # slash at the end of the url

# Data Base Config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Cambia esto al URI de tu base de datos
db.init_app(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt() 

# Función para crear o migrar las tablas en la base de datos
def create_or_migrate_db():
    with app.app_context():
        db.create_all()

# Definición de endpoints de prueba
@app.route('/')
def hello_world():
    return jsonify(message='Welcome Home')

# USER SIGNUP
@app.route('/signup', methods=['POST'])
#@jwt_required() # SOLO ADMINS
def signup_user():
    body = json.loads(request.data)
    #pw_hash = current_app.bcrypt.generate_password_hash(body["password"]).decode('utf-8') # NO

    # user exist ?
    user = User.query.filter_by(email=body["email"]).first()
    if user is None:  
        # hashing the password
        #hashed_password = bcrypt.hashpw(body["password"].encode('utf-8'), bcrypt.gensalt()) # NO
        #hashed_password = api.bcrypt.generate_password_hash(body["password"]).decode('utf-8') # NO
        hashed_password = bcrypt.generate_password_hash(body["password"]).decode('utf-8')

        new_user = User(
            name=body["name"],
            last_name=body["last_name"],
            email=body["email"],
            #password=body["password"],
            password= hashed_password,
            is_active=body["is_active"],
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "User created."}), 200
    
    return jsonify({"msg": "User already exists."}), 400


# USER LOGIN
@app.route('/login', methods=['POST'])  
def login_user():

  email = request.json.get('email', None)
  password = request.json.get('password', None)

  user = User.query.filter_by(email=email).first()
  if not user or not bcrypt.check_password_hash(user.password, password): #check hashed password
    return jsonify({'msg': 'Invalid username/password'}), 401

  access_token = create_access_token(identity=email)

  return jsonify(access_token=access_token, 
                 user_id=user.id,
                 user_name = user.name,
                 user_last_name = user.last_name,
                 user_email = user.email
                 ), 200


# muestra todos los usuarios
@app.route('/users', methods=['GET'])
#@jwt_required()
def get_users():
    # email=get_jwt_identity()
    user = User.query.all()
    results = list(map(lambda usuarios: usuarios.serialize(), user))

    if user is None:
        return jsonify({"msg": "no existen usuarios"}), 404
    return jsonify(results), 200



if __name__ == "__main__":
    generate_sitemap()  # Genera el sitemap cuando se ejecuta el servidor
    create_or_migrate_db()  # Crea o migra la base de datos al ejecutar el servidor
