/* ¿Que tipo de entidades? productos
Nombre : productos
*/

Codigo
Nombre
Stock
Costo
Precio

columna y el tipo de dato
CREATE TABLE productos(
  codigo INT,
  nombre VARCHAR(50),
  Stock INT,
  Costo FLOAT,
  Precio FLOAT
);

codigo INT
nombre VARCHAR(50)
Stock INT
Costo FLOAT
Precio FLOAT

#No importa el orden de las columnas
#Si importa el orden en Value ya que cada elemento se le asiganará
a la columna determinada en el oden del INSERT
#No es necesario que si o si pongamos todas las columnas
INSERT INTO productos(codigo, nombre, Stock, Costo, Precio )
VALUES (001, "Manzana", 20, 2500, 1000),
       (001, "Banana", 2, 2200, 2500),
       (001, "Durazno", 2, 3000, 3500),
       (001, "Lechuga", 3, 1500, 2200),
       (001, "Tomate", 2, 2000, 2500),
       (001, "Zapallo", 2, 2200, 2600),
       (001, "Repollo Blanco", 1, 2500, 2800);
