from pydantic import BaseModel
from datetime import date
class Item(BaseModel):
    usuario_id: int
    libro_id: int
    fecha_prestamo: date
    fecha_devolucion: date
