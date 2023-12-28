# uvicorn main:app --reload http://127.0.0.1:8000
from fastapi import Depends, FastAPI, HTTPException
from database.database import engine, get_db
from sqlalchemy.orm import Session
from operations import route_operations
from database import schemas, models
from login import login
from typing import List
models.Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(login.router)

# Obtener tabla 'clientes' completa.
@app.get("/clientes", response_model=List[schemas.Cliente])
async def table_clientes(db: Session = Depends(get_db)):
    db_cliente = route_operations.get_all_clientes(db)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Tabla no encontrada")
    return db_cliente

# Obtener tabla 'productos' completa.
@app.get("/productos", response_model=List[schemas.Producto])
async def table_productos(db: Session = Depends(get_db)):
    db_producto = route_operations.get_all_productos(db)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Tabla no encontrada")
    return db_producto

# Filtrar tabla 'clientes' por id_cliente.
@app.get("/clientes/id_cliente={id_cliente}", response_model=List[schemas.Cliente])
async def costumer_by_id(id_cliente: int, db: Session = Depends(get_db)):
    db_cliente = route_operations.get_customer_by_id(db, id_cliente)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

# Filtrar tabla 'productos' por id_producto.
@app.get("/productos/id_producto={id_producto}", response_model=List[schemas.Producto])
async def product_by_id(id_producto: int, db: Session = Depends(get_db)):
    db_producto = route_operations.get_product_by_id(db, id_producto)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto

# Filtrar tabla 'clientes' por país.
@app.get("/clientes/pais={pais}", response_model=List[schemas.Cliente])
async def costumer_by_country(pais: str, db: Session = Depends(get_db)):
    db_cliente = route_operations.get_customer_by_country(db, pais)
    if db_cliente is None:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return db_cliente

# Filtrar tabla 'productos' por pais_origen.
@app.get("/productos/pais_origen={pais_origen}", response_model=List[schemas.Producto])
async def product_by_id(pais_origen: str, db: Session = Depends(get_db)):
    db_producto = route_operations.get_product_by_country(db, pais_origen)
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return db_producto
