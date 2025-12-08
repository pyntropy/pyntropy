INSERT INTO steps (is_active,
                   module_id,
                   step_order,
                   slug,
                   title,
                   summary)
VALUES (TRUE, 1, 1, 'introduction-to-redis', 'Шаг 1: Введение. Зачем аналитику разбираться в Redis?',
        'Разберемся что такое Redis и какие задачи решает.'),
       (TRUE, 1, 2, 'theory-of-caching', 'Шаг 2: Теория кеширования — основа основ',
        'Изучим паттерны и проблемы')

