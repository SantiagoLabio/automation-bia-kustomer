from fastapi import APIRouter, Request, HTTPException
from app.db.session import get_db_connection
import json

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "success", "message": "Healthy"}

@router.post("/assigned-users")
async def lambda_handler(request: Request):
    try:
        body = await request.json()  # Obtener el cuerpo de la solicitud

        # Extraer datos del cuerpo
        id = body.get('id')
        codigo_interno_bia = body.get('codigo_interno_bia')
        customer_manager = body.get('customer_manager')
        customer_agent = body.get('customer_agent')

        if not all([id, codigo_interno_bia, customer_manager, customer_agent]):
            raise HTTPException(status_code=400, detail="Faltan campos obligatorios")

        # Conectar a la base de datos y ejecutar la consulta
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO pipefy.kustomer_services (id, codigo_interno_bia, customer_manager, customer_agent) VALUES (%s, %s, %s, %s)',
            (id, codigo_interno_bia, customer_manager, customer_agent)
        )
        conn.commit()
        cursor.close()
        conn.close()

        return {'message': 'Datos recibidos y almacenados'}

    except Exception as err:
        raise HTTPException(status_code=500, detail=f"Error al almacenar datos: {err}")
    


@router.get("/health")
def health_check():
    return {"status": "success", "message": "Healthy"}