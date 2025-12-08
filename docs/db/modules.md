Таблица "Модули" содержит список учебных модулей.

- **id** integer not null - id модуля.
- **domain_id** integer not null - id модуля.
- **module_order** integer not null - порядковый номер модуля в доменее.
---
- **title** varchar(100) not null - название модуля.
- **slug**  varchar(50) not null - читаемый ключ для URL модуля.
- summary text - краткое описание модуля (не более 255 символов
- description text - описание модуля в формате markdown..
- objectives text - цель модуля в формате markdown.
- prerequisites text - предварительные требования к модулю в формате markdown.