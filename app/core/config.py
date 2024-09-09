from dotenv import load_dotenv
import os

# Cargar las variables de entorno
load_dotenv()

class Settings:
    DB_USER = os.getenv('DB_USER')
    DB_HOST = os.getenv('DB_HOST')
    DB_NAME = os.getenv('DB_NAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_PORT = os.getenv('DB_PORT')

    def __init__(self):
        if not all([self.DB_USER, self.DB_HOST, self.DB_NAME, self.DB_PASSWORD, self.DB_PORT]):
            raise ValueError("Una o más variables de entorno necesarias no están definidas.")

settings = Settings()
