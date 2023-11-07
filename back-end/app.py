from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'

def create_db():
    with app.app_context():
        db.create_all()

# ejecuta el back-end
if __name__ == '__main__':
    from routes import *
    create_db()
    app.run()
