INSERT INTO domains (is_active, slug, title, summary, description)
VALUES (TRUE,
        'databases',
        'Базы данных',
        'Изучим самую популярную NO-SQL базу данных ключ-значение.',
        'Установим, подключимся и попрактикуемся на Python.');

select nextval('domains_id_seq')

update domains set
 is_active = true where id = 1