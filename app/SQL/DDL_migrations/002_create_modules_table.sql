CREATE TABLE IF NOT EXISTS modules
(
    id            SERIAL PRIMARY KEY,
    updated_at    TIMESTAMP    NOT NULL DEFAULT NOW(),
    is_active     BOOLEAN      NOT NULL DEFAULT FALSE,
    domain_id     INTEGER      NOT NULL,
    module_order  INTEGER      NOT NULL,
    slug          VARCHAR(100) NOT NULL,
    title         VARCHAR(100) NOT NULL,
    summary       TEXT,
    description   TEXT,
    objectives    TEXT,
    prerequisites TEXT
);

ALTER TABLE modules
    ADD CONSTRAINT fk_modules_domain_id
        FOREIGN KEY (domain_id)
            REFERENCES domains (id);

