INSERT INTO modules (domain_id,
                     is_active,
                     module_order,
                     slug,
                     title,
                     summary,
                     description,
                     objectives,
                     prerequisites)
VALUES (1,
        TRUE,
        1,
        'redis',
        'Redis',
        'Изучим самую популярную NO-SQL базу данных ключ-значение.',
        'Установим, подключимся и попрактикуемся на Python.',
        'Понимание и еще раз понимание',
        'Знание Python');

select * from modules;