-- select name, email from loozers;
-- этот запрос выбирает только два столба имя и почту


-- select * from loozers where name = 'Irina Kairatovna';
-- Запрос с выборкой использует оператор (WHERE) и дает 
-- результат из таблицы по запрашиваемому имени. 


-- select * from loozers order by name;
-- этот вид выборки сортирует таблицу по столбцу имени 
-- в алфавитном порядке.


-- select * from loozers order by registration_date desc;
-- данная выборка с сортировкой по дате регистрации в обратном 
-- порядке за счет функции DESC.


-- select * from loozers where email like 'bekov%';
-- выборка с использованием оператора like дает возможность 
-- поиска данных с определенной последовательностью символов, 
-- знак % это спец символ, который означает любое количество 
-- символов.


-- select count(*) as total_loozers from loozers;
-- функция cjunt(*) - это агрегатная функция, которая считывает все 
-- все строки. as total_loozers задает псевдоним для этого столбца.


-- select distinct name from loozers;
-- выборка с поиощью оператора distinct  возвращает уникальные значения
-- столбца указанного столбца, в нашем случае столбца name.


-- select * from  loozers limit 3;
-- limit определяет ограниченное количество строк, в нашем случае первые 3.


select * from loozers where name = 'Irina Kairatovna' and registration_date > '2024-09-20';
-- условные операторы and/or дают возможность комбинировать несколько условии при выборке. 




