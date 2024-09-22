-- ОБНОВЛЕНИЕ ОДНОГО ПОЛЯ ДЛЯ ОДНОЙ ЗАПИСЕЙ
/*update loozers 
set email = 'bek.bekov@newdomain.com'
where name = 'Bek Bekov';*/

-- команда update указывает на обновления
-- set указывает что будем менять поле email на новое значение 'bek.bekov.com'
-- where name это условие, что замена будет только для имени 'Bek Bekov'.

--ОБНОВЛЕНИЕ НЕСКОЛЬКИХ ПОЛЕЙ ДЛЯ ОДНОЙ ЗАПИСИ
update loozers
set name = 'Irina Kairatovna', email = 'irina.kairatovna@mail.com'
where loozer_id = 3;
-- name и email одновременно обновляемые поля, определены оператором set
-- условие where loozer_id = 3 указывает, 
-- что обновления будут применяться только к записи loozer_id = 3 

-- ОБНОВЛЕНИЕ ДAННЫХ ДЛЯ НЕСКОЛЬКИХ ЗАПИСЕЙ
 --update loozers 
 --set email = replace (email, 'example.com', 'domain.com')
 --where email like '%example.com';


 
