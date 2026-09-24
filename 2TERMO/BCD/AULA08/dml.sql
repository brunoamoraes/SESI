-- Active: 1788435081206@@127.0.0.1@3306@smartcoffee_dml_bruno
-- BANCO DE DADOS - SMARTCOFFEE - DML
-- RECURSO DE RESET DE BANCO DE DADOS
DROP DATABASE IF EXISTS SMARTCOFFEE_DML_BRUNO;
CREATE DATABASE IF NOT EXISTS SMARTCOFFEE_DML_BRUNO;
USE SMARTCOFFEE_DML_BRUNO;

CREATE TABLE cliente (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE,
    telefone VARCHAR(15),
    cidade VARCHAR(60) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE categoria (
    id_categoria INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE produto (
    id_produto INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    ativo BOOLEAN NOT NULL DEFAULT TRUE,
    id_categoria INT NOT NULL,
    CONSTRAINT fk_produto_categoria FOREIGN KEY (id_categoria) REFERENCES categoria (id_categoria)
);

CREATE TABLE pedido (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    data_pedido DATETIME NOT NULL,
    status_pedido ENUM('ABERTO','PREPARANDO','FINALIZADO','CANCELADO') NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    id_cliente INT NOT NULL,
    CONSTRAINT fk_pedido_cliente FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente)
);

CREATE TABLE item_pedido (
    id_item INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10,2) NOT NULL,
    observacao VARCHAR(150),
    CONSTRAINT fk_item_pedido FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido),
    CONSTRAINT fk_item_produto FOREIGN KEY (id_produto) REFERENCES produto (id_produto)
);

CREATE TABLE forma_pagamento (
    id_forma_pagamento INT PRIMARY KEY AUTO_INCREMENT,
    descricao VARCHAR(40) NOT NULL UNIQUE
);

CREATE TABLE pagamento (
    id_pagamento INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT NOT NULL,
    id_forma_pagamento INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    data_pagamento DATETIME,
    CONSTRAINT fk_pagamento_pedido FOREIGN KEY (id_pedido) REFERENCES pedido (id_pedido),
    CONSTRAINT fk_pagamento_forma_pagamento FOREIGN KEY (id_forma_pagamento) REFERENCES forma_pagamento (id_forma_pagamento)
);

-- INSERINDO DADOS NO BD
INSERT INTO cliente (nome, email, telefone, cidade, ativo) VALUES
('Luis Felipe','luis@email.com','1999999901','Limeira',TRUE),
('Maria Eduarda','maria@email.com','1999999902','Limeira',TRUE),
('Mateus Silva','mateus@email.com','1999999903','Limeira',TRUE),
('Matheus Oricolli','matheusc@email.com','1999999904','Limeira',TRUE),
('Nicolas Filipe','nicolas@email.com','1999999906','Limeira',TRUE),
('Otavio Correia','otavio@email.com','1999999905','Conchal',TRUE),
('Pedro Miranda','pedro@email.com','1999999907','Limeira',TRUE),
('Rafael Viera','rafael@email.com','1999999908','Limeira',TRUE),
('Rebecca','rebecca@email.com',NULL,'Limeira',TRUE),
('Rennan Campos','rennan@email.com','1999999909','Americana',TRUE),
('Samira Emily Dalosto','samira@email.com',NULL,'Ourinhos',FALSE),
('Sophia Carolina','sophia@email.com','1999999911','Taubaté',TRUE),
('Stefany Santana','stefany@email.com',NULL,'Campinas',FALSE),
('Vanessa Queiroz','vanessa@email.com','1999999912','Limeira',TRUE),
('Vinicius Henrique','vinicius@email.com','1999999913','Limeira',TRUE),
('Vinicius Oliveira','viniciuso@email.com','1999999914','Chicago',TRUE);

SELECT * FROM produto;

INSERT INTO categoria (nome) VALUES
('Café'),('Bebidas Quentes'),('Bebidas Geladas'),('Doces'),('Salgados'),('Combo');

INSERT INTO produto (nome, preco, ativo, id_categoria) VALUES
('Café Expresso', 5.00, TRUE, 1),
('Cappuccino', 7.50, TRUE, 2),
('Chocolate Quente', 6.00, TRUE, 2),
('Chá Gelado', 4.50, TRUE, 3),
('Suco Natural', 5.50, TRUE, 3),
('Bolo de Chocolate', 8.00, TRUE, 4),
('Torta de Limão', 9.00, TRUE, 4),
('Pão de Queijo', 3.50, TRUE, 5),
('Croissant', 4.00, TRUE, 5),
('Combo Café da Manhã', 15.00, TRUE, 6);

INSERT INTO pedido (data_pedido, status_pedido, valor_total, id_cliente) VALUES
(NOW(),'ABERTO',0.00,1),
('2026-10-02 08:30:00','FINALIZADO',0.00,1),
(NOW(),'ABERTO',0.00,1);

INSERT INTO item_pedido (id_pedido, id_produto, quantidade, preco_unitario, observacao) VALUES
(1, 1, 2, 5.00, 'Sem açúcar'),
(1, 6, 1, 8.00, NULL),
(2, 2, 1, 7.50, 'Com canela'),
(2, 4, 2, 4.50, NULL),
(3, 10, 1, 15.00, 'Sem ovo');

INSERT INTO forma_pagamento (descricao) VALUES
('Dinheiro'),('Cartão de Crédito'),('Cartão de Débito'),('Pix');

INSERT INTO pagamento (id_pedido, id_forma_pagamento, valor, data_pagamento) VALUES
(2, 2, 19.50, '2026-10-02 08:45:00'),
(2, 4, 0.00, NOW()),
(3, 4, 15.00, NULL);    

----------------------------------------
-- EXEMPLO NOVO DE INSERÇÃO DE DADOS PORÉM COM RECUPERAÇÃO DO ÚLTIMO ID
INSERT INTO pedido (data_pedido, status_pedido, valor_total, id_cliente) VALUES (NOW(), 'ABERTO','0.00',1);
SET @pedido = LAST_INSERT_ID();
SELECT @pedido;

--------------------------------------------------

-- ATUALIZAÇÕES E MODIFICAÇÕES DE DADOS
-- EX 1
UPDATE cliente
SET telefone = '1999888802'
WHERE id_cliente = 9;

-- EX 2:
UPDATE produto
SET preco = 1.00;
-- NUNCA REALIZAR UM UPDATE SEM --- WHERE 😤

-- EX: 3
UPDATE cliente
SET telefone = '1997777701',
    cidade = 'Valinhos'
WHERE id_cliente = 11;

-- EX 4: Ajustes de valores
UPDATE produto
SET preco = preco * 1.05
WHERE id_categoria = 1;

-- EX 5: Ajustes de atualizações condicionais
UPDATE produto
SET preco = CASE
    WHEN preco <= 20 THEN preco * 1.20
    ELSE preco * 1.05
END
WHERE ativo = TRUE;

--------------------------------------
-- APAGAR DADOS DO BD

-- EX 1: Apagar um cliente específico
DELETE FROM cliente
WHERE id_cliente = 11;

-- EX 2 : Apagar todos os clientes inativos
DELETE FROM cliente
WHERE ativo = FALSE;

-- EX 3 : Apagar todos os clientes de uma cidade específica
DELETE FROM cliente
WHERE cidade = 'Chicago';

-- EX 4: Exclusão lógica
UPDATE cliente
SET ativo = FALSE
WHERE id_cliente = 10;

select * from cliente;

-- DESAFIOS DML
-- PARTE A
-- 1. CADASTRE DOIS NOVOS CLIENTES

