from pydantic import BaseModel
class Item(BaseModel):
    nombre: str
    direccion: str
