from app import app as application
from utils import generate_sitemap
from app import create_or_migrate_db  # Importa la función

if __name__ == "__main__":
    generate_sitemap()  # Genera el sitemap cuando se ejecuta el servidor
    create_or_migrate_db()  # Crea o migra la base de datos al ejecutar el servidor
    application.run()

#     application.run(host='0.0.0.0', port=8080)


