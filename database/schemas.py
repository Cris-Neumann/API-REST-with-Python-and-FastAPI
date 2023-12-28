# Modelos de Pydantic.
from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int
    dni: int
    nombre_cliente: str
    apellido_cliente: str
    edad: int
    pais: str
    ingreso_mensual: int

class Producto(BaseModel):
    id_producto: int
    nombre: str
    cantidad_stock: int
    pais_origen: str
    ciudad_destino: str
    precio_venta: int

class User(BaseModel):
    id: int
    email: str
    password_: str
    is_superuser: bool
    is_active: bool

class Token(BaseModel):
    access_token: str
    token_type: str