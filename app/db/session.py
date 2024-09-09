import psycopg2
from app.core.config import settings

# Configuración de la conexión a PostgreSQL desde las variables de entorno
db_config = {
    'user': settings.DB_USER,
    'host': settings.DB_HOST,
    'database': settings.DB_NAME,
    'password': settings.DB_PASSWORD,
    'port': int(settings.DB_PORT)
}

def get_db_connection():
    return psycopg2.connect(
        user=db_config['user'],
        host=db_config['host'],
        database=db_config['database'],
        password=db_config['password'],
        port=db_config['port']
    )
