CREATE TABLE IF NOT EXISTS steps
(
    id          SERIAL PRIMARY KEY,
    updated_at  TIMESTAMP    NOT NULL DEFAULT NOW(),
    is_active   BOOLEAN      NOT NULL DEFAULT FALSE,
    module_id   INTEGER      NOT NULL,
    step_order  INTEGER      NOT NULL,
    slug        VARCHAR(100) NOT NULL,
    title       VARCHAR(100) NOT NULL,
    summary     TEXT,
    description TEXT,
    objectives  TEXT,
    content     TEXT
);

ALTER TABLE steps
    ADD CONSTRAINT fk_steps_module_id
        FOREIGN KEY (module_id)
            REFERENCES modules (id);

ALTER TABLE steps
    ADD UNIQUE (module_id, step_order);

