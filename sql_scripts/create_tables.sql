CREATE TABLE clientes (
    id_cliente INT PRIMARY KEY IDENTITY (1, 1),
    dni INT NOT NULL,
    nombre_cliente VARCHAR(50),
    apellido_cliente VARCHAR(50),
    edad INT,
    pais VARCHAR (100),
    ingreso_mensual INT);
INSERT INTO clientes
VALUES  (43986759, 'Juan', 'Perez', 45, 'Chile', 2300000),
        (35310078, 'Maria', 'Gonzalez', 53, 'Perú', 1250000),
        (47790587, 'Fernando', 'Frei', 37, 'Chile', 8000000),
        (44354488, 'Maria', 'Ulloa', 28, 'Argentina', 750000),
        (49468628, 'Luis', 'Vidal', 44, 'Chile', 180000),
        (36427593, 'Josefa', 'Larrain', 22, 'Chile', 350000);

CREATE TABLE productos (
    id_producto INT PRIMARY KEY IDENTITY (1, 1),
    nombre VARCHAR(50),
    cantidad_stock INT,
    pais_origen VARCHAR (100),
    ciudad_destino VARCHAR (100),
    precio_venta INT);
INSERT INTO productos
VALUES  ('martillo', 360, 'China', 'Santiago', 90000),
        ('cierra', 400, 'China', 'Santiago', 450000),
        ('papel mural', 150, 'India', 'Rancagua', 22000),
        ('tijeras', 2100, 'China', 'Valparaiso', 7600),
        ('pintura', 160, 'Singapur', 'Santiago', 14000);

CREATE TABLE user_api (
    id INT PRIMARY KEY IDENTITY (1, 1),
	email VARCHAR (150),
    password_ VARCHAR (150),
    is_superuser BIT,
	is_active BIT);
INSERT INTO user_api
VALUES  ('user1', '123', 1, 0),
        ('user2', '1234', 1, 0),
        ('user3', '12345', 0, 1),
        ('user4', '123456', 0, 0);
