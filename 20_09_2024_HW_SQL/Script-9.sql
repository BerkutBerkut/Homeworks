insert into loozers (name, email) values
('Petr Petrov', 'petrov@example.com'),
('Maks Maksimov', 'maksimov@example.com'),
('Irina Kairatovna', 'kairatovna@example.com'),
('Anna Antonovna', 'antonovna@example.com'),
('Bek Bekov', 'bekov@example.com');

-- Наполнение таблицы осуществляется с помощью команды insert into;
-- поле loozer_id заполняется автоматический за счет типа SERIAL;
-- поле registration_date автоматический текущее время и дата;


select * from loozers;

-- данный запрос дает возможность проверить заполнение созданой таблицы и наличие в ней заданных полей и записей.

/* insert into loozers (name, email) values
('Ivan Petrov', 'petr@example.com'),
('Ivan Ivanov', 'ivan@example.com');*/