-- Active: 1788435081206@@127.0.0.1@3306@sesi_cr_ta
-- Sql ANSI 2003 - brModelo.
-- Relacionamento e Cardinalidade - Banco de dados Exemplo

CREATE DATABASE IF NOT EXISTS SESI_CR_TA;
USE SESI_CR_TA;


CREATE TABLE Cliente (
Id_Cliente Int Auto_Increment Primary Key PRIMARY KEY,
Nome_Cliente varchar(60) not null
);

CREATE TABLE Pedido (
Id_Pedido Int Auto_Increment Primary Key PRIMARY KEY,
Data_Pedido datetime not null,
Id_Cliente Int not null,
FOREIGN KEY(Id_Cliente) REFERENCES Cliente (Id_Cliente)
);

CREATE TABLE Estoque (
Nome_Produto varchar(100) not null,
Id_Produto Int not null unique,
Id_Estoque Int Auto_Increment Primary Key,
Quantidade int not null
-- PRIMARY KEY(Id_Produto,Id_Estoque)
);

CREATE TABLE Fornecedor (
Razao_Social varchar(100) not null,
Id_Fornecedor Int Auto_Increment Primary Key PRIMARY KEY
);

CREATE TABLE Produto (
Id_Produto Int Auto_Increment Primary Key PRIMARY KEY,
Nome_Produto varchar(100) not null
);

CREATE TABLE Item_Produto (
Id_Produto Int not null,
Id_Fornecedor Int not null,
Id_Item Int Auto_Increment Primary Key PRIMARY KEY,
Valor Decimal(10,2),
Observacao Text(300),
FOREIGN KEY(Id_Produto) REFERENCES Produto (Id_Produto),
FOREIGN KEY(Id_Fornecedor) REFERENCES Fornecedor (Id_Fornecedor)
);

