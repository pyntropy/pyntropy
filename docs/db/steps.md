Таблица "Шаги" содержит контент уроков с привязкой к модулям.

- **id** integer not null - id шага.
- **module_id** integer not null - id модуля.
- **module_order** integer not null - порядковый номер шага в модуле.
- ***update_at** timestamp - время последнего обновления.
---
- **title** varchar(100) not null - название шага.
- **slug**  varchar(50) not null - читаемый ключ для URL шага.
- summary text - краткое описание модуля (не более 255 символов
- description text - описание шага.
- objectives text - цель шага.
---
- content text - контент шага.