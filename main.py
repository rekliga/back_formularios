from fastapi import FastAPI, status, Response
from pydantic import BaseModel
from schemas.Formularios import FormularioBase, RespuestaFormulario
from schemas.Responses import ErrorResponse, SuccessResponse
from settings import settings
from pymongo.mongo_client import MongoClient
from mongoengine import connect
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/registro/usuarios")
async def registro(payload: FormularioBase, response: Response):
    client = MongoClient(settings.database_url)
    connect(host=settings.database_url, db="formularios")

    try:
        registro = RespuestaFormulario(**payload.dict())
        registro.save()
        return SuccessResponse(message="Registro exitoso", status=200, data={})
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return ErrorResponse(message=f"Error al registrar {e}", status=500, data={})

    finally:
        client.close()
