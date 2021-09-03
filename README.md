Sitio Web desarrollado para el Informatorio 2011

Utilice la plantilla base: https://getbootstrap.com/docs/4.0/examples/album/

Pre-requisitos:
Instalar las dependendencias del proyecto (ir a la carpeta de requirements)
pip install -r base.txt

Crear settings local.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Conector de DB
        'NAME': 'NombreBaseDeDatos',
        'USER': 'UsuarioBaseDeDatos',
        'PASSWORD': 'ContraseñaBaseDeDatos',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

Herramientas utilizadas:
Django Framework web
PostgreSQL Base de datos

