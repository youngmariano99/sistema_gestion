-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS Sistema_Gestion_May;
USE Sistema_Gestion_May;

-- Tabla de Métodos de Pago
CREATE TABLE Payment_Methods (
    Payment_Method_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Description VARCHAR(255)
);

-- Tabla de Permisos
CREATE TABLE Permissions (
    Permission_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Description VARCHAR(255)
);

-- Tabla de Roles
CREATE TABLE Roles (
    Role_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Description VARCHAR(255),
    Permission_ID INT,
    UNIQUE (Permission_ID),
    FOREIGN KEY (Permission_ID) REFERENCES Permissions(Permission_ID)
);

-- Tabla de Usuarios
CREATE TABLE Users (
    User_ID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) UNIQUE NOT NULL,
    Password VARCHAR(255) NOT NULL,
    Role_ID INT,
    Email VARCHAR(100) UNIQUE NOT NULL,
    FOREIGN KEY (Role_ID) REFERENCES Roles(Role_ID)
);

-- Tabla de Clientes
CREATE TABLE Clients (
    Client_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Surname VARCHAR(50) NOT NULL,
    Phone VARCHAR(20) UNIQUE,
    Email VARCHAR(100) UNIQUE
);

-- Tabla de Proveedores
CREATE TABLE Suppliers (
    Supplier_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Description VARCHAR(255),
    Phone VARCHAR(20)
);

-- Tabla de Categorías de Productos
CREATE TABLE Category (
    Category_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL UNIQUE
);

-- Tabla de Marcas
CREATE TABLE Brands (
    Brand_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL UNIQUE,
    Description VARCHAR(250) 
);

-- Tabla de Productos
CREATE TABLE Products (
    Product_ID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Stock INT DEFAULT 0,
    Price DECIMAL(10,2) NOT NULL,
    Cost DECIMAL(10,2) NOT NULL,
    Category_ID INT,
    FOREIGN KEY (Category_ID) REFERENCES Category(Category_ID)
);

-- Relación entre Productos y Marcas (Muchos a Muchos)
CREATE TABLE Brands_Products (
    Product_ID INT,
    Brand_ID INT,
    PRIMARY KEY (Product_ID, Brand_ID),
    FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID),
    FOREIGN KEY (Brand_ID) REFERENCES Brands(Brand_ID)
);

-- Tabla de Ventas
CREATE TABLE Sales (
    Sale_ID INT AUTO_INCREMENT PRIMARY KEY,
    Date_Of_Purchase DATETIME NOT NULL,
    Client_ID INT,
    Total DECIMAL(10,2) NOT NULL,
    Payment_Method_ID INT,
    FOREIGN KEY (Client_ID) REFERENCES Clients(Client_ID),
    FOREIGN KEY (Payment_Method_ID) REFERENCES Payment_Methods(Payment_Method_ID)
);

-- Detalles de Ventas
CREATE TABLE Sale_Details (
    Sale_ID INT,
    Product_ID INT,
    Quantity DECIMAL(10,2) NOT NULL,
    Subtotal DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (Sale_ID, Product_ID),
    FOREIGN KEY (Sale_ID) REFERENCES Sales(Sale_ID),
    FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
);

-- Tabla de Compras
CREATE TABLE Purchases (
    Purchase_ID INT AUTO_INCREMENT PRIMARY KEY,
    Supplier_ID INT,
    Date DATETIME NOT NULL,
    Total DECIMAL(10,2) NOT NULL,
    Payment_Method_ID INT,
    FOREIGN KEY (Supplier_ID) REFERENCES Suppliers(Supplier_ID),
    FOREIGN KEY (Payment_Method_ID) REFERENCES Payment_Methods(Payment_Method_ID)
);

-- Detalles de Compras
CREATE TABLE Purchase_Details (
    Purchase_ID INT,
    Product_ID INT,
    Quantity DECIMAL(10,2) NOT NULL,
    Subtotal DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (Purchase_ID, Product_ID),
    FOREIGN KEY (Purchase_ID) REFERENCES Purchases(Purchase_ID),
    FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
);

-- Movimientos de Stock
CREATE TABLE Stock_Movements (
    Movement_ID INT AUTO_INCREMENT PRIMARY KEY,
    Product_ID INT,
    Quantity DECIMAL(10,2) NOT NULL,
    Type ENUM('Ingreso', 'Salida', 'Ajuste') NOT NULL,
    Date DATETIME NOT NULL,
    Reason VARCHAR(255),
    FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
);

-- Detalles de Movimientos de Stock
CREATE TABLE Stock_Movement_Details (
    Movement_ID INT,
    Product_ID INT,
    Quantity DECIMAL(10,2) NOT NULL,
    PRIMARY KEY (Movement_ID, Product_ID),
    FOREIGN KEY (Movement_ID) REFERENCES Stock_Movements(Movement_ID),
    FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
);

-- Insertar metodos de pagos
INSERT INTO Payment_Methods (Name, Description) VALUES
('Efectivo', 'Pago en efectivo'),
('Débito', 'Tarjeta de débito bancaria'),
('Crédito', 'Tarjeta de crédito bancaria'),
('Transferencia', 'Transferencia bancaria'),
('Mercado Pago QR', 'Pago a través de Mercado Pago Codigo QR'),
('Mercado Pago Transferencia', 'Pago a través de Mercado Pago con CBU o ALIAS'),
('Cuenta DNI QR', 'Pago digital con QR'),
('Cuenta DNI Transferencia', 'Pago digital con DNI, CBU ó ALIAS');

-- Insertar categorias de productos
INSERT INTO Category (Name) VALUES
('Bebidas'),
('Alimentos'),
('Fiambre'),
('Lácteos'),
('Frutas'),
('Verduras'),
('Productos de Limpieza'),
('Snacks'),
('Golosinas'),
('Condimentos y Especias'),
('Carnes');

-- Agregué 2 restricciones para que no pueda ser 0 tanto stock como quantity
ALTER TABLE products ADD CONSTRAINT chk_stock CHECK (Stock >= 0);
ALTER TABLE stock_movements ADD CONSTRAINT chk_quantity CHECK (Quantity > 0);

ALTER TABLE stock_movements DROP FOREIGN KEY stock_movements_ibfk_1;
ALTER TABLE stock_movements DROP COLUMN Product_ID;



