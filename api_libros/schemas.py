from pydantic import BaseModel
class Item(BaseModel):
    titulo: str
    autor: str
    genero: str
    disponibilidad: bool
