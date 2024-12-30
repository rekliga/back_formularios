
from pydantic import BaseModel
import mongoengine as me
from datetime import datetime

class FormularioBase(BaseModel):
    nombre: str 
    id_promocion: str
    email: str
    telefono: str
    ocupacion: str
    mensaje: str


class RespuestaFormulario(me.Document):
    nombre = me.StringField(required=True, max_length=255)
    id_promocion = me.StringField(required=True, max_length=255)
    email = me.EmailField(required=True)
    mensaje = me.StringField(required=True)
    fecha_registro = me.DateTimeField(default=datetime.utcnow)
    ocupacion = me.StringField(required=True, max_length=255)
    telefono = me.StringField(required=True, max_length=255)
    meta = {
        'collection': 'respuestas_formulario',
        'indexes': [
            {'fields': ['email', 'id_promocion'], 'unique': True}  # Índice único en email
        ]
    }
