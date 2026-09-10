-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



CREATE TABLE Cliente (
Id_Cliente Int Auto_Increment Primary Key PRIMARY KEY,
Nome_Cliente varchar(60) not null
)

CREATE TABLE Pedido (
Id_Pedido Int Auto_Increment Primary Key PRIMARY KEY,
Data_Pedido datetime not null,
Id_Cliente Int Auto_Increment Primary Key,
FOREIGN KEY(Id_Cliente) REFERENCES Cliente (Id_Cliente)
)

CREATE TABLE Estoque (
Id_Produto Int Auto_Increment Primary Key,
Nome_Produto varchar(100) not null,
Id_Estoque Int Auto_Increment Primary Key,
Quantidade int not null,
PRIMARY KEY(Id_Produto,Id_Estoque)
)

CREATE TABLE Fornecedor (
Id_Fornecedor Int Auto_Increment Primary Key PRIMARY KEY,
Razao_Social varchar(100) not null
)

CREATE TABLE Produto (
Id_Produto Int Auto_Increment Primary Key PRIMARY KEY,
Nome_Produto varchar(100) not null
)

CREATE TABLE Item_Produto (
Id_Produto Int Not Null,
Id_Fornecedor Int Not Null,
Id_Item Int Auto_Increment Primary Key PRIMARY KEY,
Valor Decimal(10,2)
)

