CREATE TABLE IF NOT EXISTS domains
(
    id          SERIAL PRIMARY KEY,
    updated_at  TIMESTAMP    NOT NULL DEFAULT NOW(),
    is_active   BOOLEAN      NOT NULL DEFAULT FALSE,
    slug        varchar(100) NOT NULL,
    title       varchar(100) NOT NULL,
    summary     TEXT,
    description TEXT
);