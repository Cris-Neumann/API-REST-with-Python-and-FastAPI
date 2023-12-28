# Modelos de SQLAlchemy.
from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base

class clientes(Base):
    __tablename__ = "clientes"
    id_cliente = Column(Integer, primary_key=True, index=True)
    dni = Column(Integer)
    nombre_cliente = Column(String)
    apellido_cliente = Column(String)
    edad = Column(Integer)
    pais = Column(String)
    ingreso_mensual = Column(Integer)

class productos(Base):
    __tablename__ = "productos"
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    cantidad_stock = Column(Integer)
    pais_origen = Column(String)
    ciudad_destino = Column(String)
    precio_venta = Column(Integer)

class User(Base):
    __tablename__ = "user_api"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password_ = Column(String)
    is_superuser = Column(Boolean())
    is_active = Column(Boolean())