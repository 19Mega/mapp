from flask import jsonify, url_for

class APIException(Exception):
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {
            'message': self.message,
            'status_code': self.status_code
        }

def generate_sitemap():
    # Lista de URLs de tu sitio web
    urls = [
        '/',
        '/about',
        '/contact',
        '/products',
        # Agrega más URLs aquí según la estructura de tu sitio
    ]

    # Inicio del archivo XML del sitemap
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    # Agrega cada URL al archivo XML
    for url in urls:
        sitemap_xml += f'  <url>\n'
        sitemap_xml += f'    <loc>https://www.tusitio.com{url}</loc>\n'  # Reemplaza con tu dominio
        sitemap_xml += f'  </url>\n'

    # Fin del archivo XML del sitemap
    sitemap_xml += '</urlset>\n'

    # Guarda el archivo XML en el disco
    with open('sitemap.xml', 'w') as sitemap_file:
        sitemap_file.write(sitemap_xml)
