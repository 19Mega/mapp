from app import app as application
from utils import generate_sitemap

if __name__ == "__main__":
    generate_sitemap()  # Genera el sitemap cuando se ejecuta el servidor
    application.run()



# if __name__ == "__main__":
#     application.run(host='0.0.0.0', port=8080)
