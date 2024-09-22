create table if not exists loozers (
	loozer_id SERIAL primary key, 
	name VARCHAR(100), 
	email VARCHAR(100) unique,  
	registration_date TIMESTAMP default CURRENT_TIMESTAMP 
);

-- Создание таблицы loozers 
-- таблица создается командой create table, желательно использовать условие if not exists;
-- в () определяются поля, которые являются столбцами таблицы
-- поле loozer_id определяет идентификационный номер записи
-- тип SERIAL автоматический увеличивает значение с каждым новым пользователем;
-- primary key означает, что это будет уникальным для каждой строки;
-- name - это поле ИМЕНИ, а VARCHAR(100) - это тип данных для текстовой строки длиной не более 100 символов;
-- email - это поле эл адреса, где unique указывает на уникальность записи, другой такой не может быть.
-- registration_date TIMESTAMP - это поле для хранения даты и времени регистрации;
--  default CURRENT_TIMESTAMP - автоматический присваивает текущее время в момент добавления записи. 

