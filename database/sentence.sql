DROP DATABASE almacen_may;
CREATE DATABASE almacen_may;

USE almacen_may;

CREATE TABLE IF NOT EXISTS productos(
  codigo_producto INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(50) NOT NULL,
  stock INT UNSIGNED NOT NULL,
  costo FLOAT(6, 2) UNSIGNED NOT NULL,
  precio FLOAT(6, 2) UNSIGNED  NOT NULL,
  fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE F NOT EXISTS ventas(
  codigo_venta INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  codigo_producto INT UNSIGNED,
  nombre VARCHAR(50) NOT NULL,
  cantidad INT UNSIGNED NOT NULL,
  precio FLOAT(6, 2) UNSIGNED  NOT NULL,
  total FLOAT(6, 2) UNSIGNED  NOT NULL,
  fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (codigo_producto) REFERENCES productos(codigo_producto) ON DELETE CASCADE
  FOREIGN KEY (codigo_cliente) REFERENCES clientes(codigo_cliente) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS clientes(
  codigo_cliente INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  email VARCHAR(100) UNIQUE,
  telefono VARCHAR(20),
  direccion VARCHAR(150),
  fecha_nacimiento DATE,
  notas TEXT,
  fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO productos( nombre, stock, costo, precio )
VALUES ( "Manzana", 20, 2500, 1000),
       ( "Banana", 2, 2200, 2500),
       ( "Durazno", 2, 3000, 3500),
       ( "Lechuga", 3, 1500, 2200),
       ( "Tomate", 2, 2000.50, 2500),
       ( "Zapallo", 2, 2200.00, 2600),
       ( "Repollo Blanco", 1, 2500, 2800);

INSERT INTO ventas(codigo_producto ,nombre, cantidad, precio, total )
VALUES ( 1,"Manzana", 2, 2500, 5000),
       ( 1,"Manzana", 3, 2500, 7500),
       ( 5,"Tomate", 2, 2500, 5000),
       ( 6,"Zapallo", 2, 2500, 5000),
       ( 6,"Zapallo", 2, 2500, 5000),
       ( 6,"Zapallo", 2, 2500, 5000),
       ( 1,"Manzana", 2, 2500, 5000),
       ( 7,"Repollo Blanco", 2, 2500, 5000),
       ( 1,"Manzana", 2, 2500, 5000),
       ( 7,"Repollo Blanco", 2, 2500, 5000);
SELECT * FROM productos;
SELECT * FROM ventas;
