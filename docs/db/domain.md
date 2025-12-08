Таблица "Домены" содержит список доменов.

Пример домена: базы данных, обмен сообщениями.

- **id** integer not null - id шага.
- **is_active** bool not null - признак активности домена
- **slug** varchar(100) not null - url домена.
- **title** varchar(100) not null - название домена.
---
- summary text - краткое описание домена.
- description text - описание домена.
