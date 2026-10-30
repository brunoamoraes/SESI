
SELECT  
    U.id_usuario,
    U.nome,
    COUNT(ep.id_emprestimo) AS total_pendente
FROM usuario AS U
INNER JOIN emprestimo AS ep ON U.id_usuario = ep.id_usuario

GROUP BY 
    U.id_usuario, 
    U.nome;

SELECT L.titulo, COUNT(ep.id_emprestimo) AS vezes_emprestado
FROM livro AS L
INNER JOIN emprestimo AS ep ON L.id_livro = ep.id_livro
WHERE ep.status_emprestimo = 'Aberto'
GROUP BY L.id_livro, L.titulo;




-- 18 

SELECT  ep.id_emprestimo, U.nome,L.titulo,ep.data_emprestimo,ep.status_emprestimo 
FROM emprestimo as ep 
INNER JOIN usuario as U
INNER JOIN livro as L 
WHERE status_emprestimo = 'Aberto';


-- 19