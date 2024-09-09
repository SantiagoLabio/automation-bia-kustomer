from fastapi import FastAPI
from app.api.v1.kustomer_routes import router as kustomer_router

app = FastAPI()

# Incluir las rutas del kustomer
app.include_router(kustomer_router, prefix="/ms-asigned-tickets", tags=["Kustomer"])
