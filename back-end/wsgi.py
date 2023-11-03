from app import app as application
from models import db

if __name__ == '__main__':
    db.create_all()
    application.run()
