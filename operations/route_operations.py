from sqlalchemy.orm import Session
from database import models

def get_all_clientes(db: Session):
    return db.query(models.clientes).all()

def get_all_productos(db: Session):
    return db.query(models.productos).all()

def get_customer_by_id(db: Session, id_customer: int):
    return db.query(models.clientes).filter(models.clientes.id_cliente == id_customer).\
    order_by(models.clientes.id_cliente).offset(0).all()

def get_product_by_id(db: Session, id_product: int):
    return db.query(models.productos).filter(models.productos.id_producto == id_product).\
    order_by(models.productos.id_producto).offset(0).all()

def get_customer_by_country(db: Session, country: str):
    return db.query(models.clientes).filter(models.clientes.pais == country).\
    order_by(models.clientes.pais).offset(0).all()

def get_product_by_country(db: Session, country: str):
    return db.query(models.productos).filter(models.productos.pais_origen == country).\
    order_by(models.productos.pais_origen).offset(0).all()
