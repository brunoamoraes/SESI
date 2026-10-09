-- Active: 1788435081206@@127.0.0.1@3306@smartcoffee_dml_bruno
-- AULA 09 - DQL (DATA QUERY LANGUAGE) - LINGUAGEM DE CONSULTA DE DADOS
-- EX 1: SELECT SIMPLES
-- SELECT coluna
-- FROM tabela;

SELECT * FROM cliente;
-- CONSULTA TODAS AS COLUNAS NA TABELA

SELECT nome, telefone FROM cliente;
SELECT nome, ativo FROM produto;
-- CONSULTA DADOS COM VÁRIAS COLUNAS

-- EX 2: CONSULTADO E PERSONALIZANDO A CONSULTA
SELECT nome AS Nome_Cliente, telefone AS Contato_Cliente
FROM cliente;

SELECT nome, preco, preco * 2.00 AS preco_ajustado
FROM produto;

-- EX 3: DISTINCT - ELIMINAR REPETIÇÕES
SELECT DISTINCT cidade
FROM cliente;
SELECT cidade FROM cliente;
-- COM DISTINCT CADA RESULTADO É APRESENTADO UMA ÚNICA VEZ
-- SEM DISTINCT CADA RESULTADO É APRESENTAOD VÁRIAS VEZES

-- EX 4: USO DE WHERE - FILTRO DE REGISTROS
-- INSERIR CONDIÇÕES E UTILIZAR OPERADORES DE COMPARAÇÃO
-- = IGUAL
-- <> OU != DIFERENTE
-- > MAIOR QUE
-- >= MAIOR OU IGUAL
-- < MENOR QUE
-- <= MENOR OU IGUAL
SELECT nome, preco FROM produto WHERE preco > 10;
-- CONSULTAR PRECOS QUE POSSUEM VALOR ACIMA DE 10.00 REAIS

SELECT nome, preco FROM produto WHERE ativo = TRUE;
-- CONSULTAR PRODUTOS ATIVO OU INATIVOS

SELECT id_pedido, data_pedido, valor_total
FROM pedido WHERE valor_total >= 25.00;
-- CONSULTAR VALOR TOTAL DE PRODUTOS ACIMA DE 25.00 REAIS

-- EX 5: USO DE AND, OR E NOT
-- AND - TODAS AS CONDIÇÕES VERDADEIRAS
SELECT nome, preco FROM produto
WHERE preco >= 8.00 AND preco <= 25.00;

-- OR - UMA DAS CONDIÇÕES PRECISA SER VERDADEIRA
SELECT nome, cidade FROM cliente
WHERE cidade = 'Limeira' OR cidade = 'Boston';

-- NOT CRIAR UM CONDIÇÃO DE NEGAÇÃO
SELECT nome, cidade FROM cliente
WHERE NOT cidade = 'Limeira';

-- AND E OR JUNTOS PRECISAMOS INSERIR ()
SELECT nome, cidade, ativo FROM cliente
WHERE ativo = TRUE AND (cidade = 'Limeira' OR cidade = 'Piracicaba');

-- EX 6: BETWEEN - PESQUISAR POR INTERVALOS
-- LIMITE INICIAL E FINAL
SELECT nome, preco FROM produto 
WHERE preco BETWEEN 8.00 AND 15.00;
-- CONSULTAR POR INTERVALO DE VALORES

SELECT id_pedido, data_pedido, valor_total
FROM pedido
WHERE data_pedido BETWEEN '2026-01-01 00:00:00' AND '2026-09-30 23:59:59';
-- CONSULTAR DADOS POR INTERVALO DE DATA

-- EX 7: IN - MUITAS POSSIBILIDADES
SELECT nome, cidade FROM cliente
WHERE cidade IN ('Limeira','Piracicaba','Americana');

SELECT nome, cidade FROM cliente
WHERE cidade NOT IN ('Limeira','Piracicaba');

-- EX 8: LIKE - PESQUISA POR TEXTOS
-- CORINGAS
-- % VÁRIOS CARACTERES
-- _ APENAS UM CARACTER
SELECT nome FROM produto
WHERE nome LIKE 'Café%';
-- CONSULTA PELA PALAVRA QUE DESEJA E QUAL COMEÇA

SELECT nome FROM produto
WHERE nome LIKE '%chocolate%';
-- CONSULTA PELA PALAVRA QUE CONTEM CHOCOLATE

SELECT nome FROM cliente
WHERE nome LIKE '%Silva';

SELECT nome FROM produto
WHERE nome LIKE '%o_o%';

-- EX 9: NULL - AUSÊNCIA DE VALOR
SELECT nome, telefone FROM cliente
WHERE telefone IS NULL;

SELECT nome, telefone FROM cliente
WHERE telefone IS NOT NULL;

SELECT nome, telefone FROM cliente
WHERE telefone = 'NULL';

-- EX 10: ORDER BY - ORDENAR RESULTADOS
-- ASC É CRESCENTE 
-- DESC É DECRESCENTE
SELECT nome, preco FROM produto
ORDER BY preco ASC;

SELECT nome, preco FROM produto
ORDER BY preco DESC;

SELECT nome, preco FROM produto
ORDER BY nome ASC , preco DESC;

SELECT cidade, nome FROM cliente
ORDER BY cidade ASC, nome DESC;
-- ORDERNAR POR MAIS DE UMA COLUNA

-- EX 11 : LIMIT DETERMINAR UMA QUANTIDADE DE LINHAS
SELECT nome, preco 
FROM produto 
ORDER BY preco DESC
LIMIT 10;

SELECT nome, preco
FROM produto
ORDER BY nome
LIMIT 10 OFFSET 5;

-- EX 12: CÁLCULOS EM COLUNAS
SELECT nome, preco, preco * 1.30 AS Preço_Reajuste
FROM produto;

SELECT id_item, quantidade, preco_unitario, quantidade * preco_unitario AS Subtotal FROM item_pedido;

-- EX 13: FUNÇÕES
-- TEXTOS
SELECT UPPER(nome) AS NOME_M , LOWER(cidade) AS cidade_m
FROM cliente;
-- USO DE MAIUSCULO E MINUSCULO
SELECT CONCAT(nome, ' -- ', cidade) AS Cliente_Cidades
FROM cliente;

-- NÚMEROS
SELECT nome, preco, ROUND(preco * 2.0 , 2) AS Preco_Desconto
FROM produto;

-- DATAS
SELECT id_pedido, data_pedido, valor_total, DATE(data_pedido) AS DATAS, MONTH(data_pedido) AS MÊS, YEAR(data_pedido) AS ANO, DAY(data_pedido) AS DIAS, TIME(data_pedido) AS Horário
FROM pedido;

-- SUBSTITUIR O NULL NO RESULTADO COM COALESCE
SELECT nome, COALESCE(telefone, 'Não Possui Telefone') AS Telefone
FROM cliente;

-- EX 14: FUNÇÕES DE AGREGAÇÃO
-- COUNT = CONTAR UMA QUANTIDADE
-- SUM = SOMAR VALORES
-- AVG = CALCULAR MÉDIA
-- MIN = MÍNIMO VALOR
-- MAX = MÁXIMO VALOR
SELECT COUNT(*) AS TOTAL_CLIENTE
FROM cliente;
-- QUANTOS CLIENTES EXISTEM NA TABELA

SELECT ROUND(AVG(preco),2) AS Preço_Médio_Produtos
FROM produto;
-- PREÇO MÉDIO DOS PRODUTOS

SELECT ROUND(MIN(preco),2) AS Preços_Baixos,
       ROUND(MAX(preco),2) AS Preço_Alto,
       ROUND(AVG(preco),2) AS Média_Preços
FROM produto;
-- RESUMO DE PREÇOS

SELECT SUM(valor_total) AS FATURAMENTO
FROM pedido
WHERE status = 'PREPARANDO';
-- TOTAL DE PEDIDOS COM CRITÉRIO

-- EX 15: GROUP BY - AGRUPAR DADOS
SELECT cidade, COUNT(*) AS QTDE_CLIENTES
FROM cliente
GROUP BY cidade;
-- QUANTOS CLIENTES TENHO EM CADA CIDADE

SELECT id_categoria, COUNT(*) AS QTDE_PRODUTOS
FROM produto
GROUP BY id_categoria;
-- QUANTIDADE DE PRODUTOS POR CATEGORIA

-- EX 16: HAVING - CRIAR CONDIÇÕES EM AGRUPAMENTOS
-- WHERE FILTRA LINHAS ANTES DO AGRUPAMENTO
-- HAVING FILTRA LINHAS DEPOIS DO GROUP BY
SELECT cidade, COUNT(*) AS QTDE_CLIENTES
FROM cliente
GROUP BY cidade
HAVING COUNT(*) <= 10;
-- CONSULTA PARA CIDADES COM PELOS MENOS DOIS CLIENTES

-- EX 17: RESUMO DE UM CONSULTA COMPLETA
-- SELECT colunas
-- FROM tabela
-- WHERE condicao
-- GROUP BY coluna_agrupar
-- HAVING condicao_agrupar
-- ORDER BY colunas
-- LIMIT quantidade;