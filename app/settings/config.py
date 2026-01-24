from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    USER: str
    PASS: str
    HOST: str
    PORT: int
    NAME: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix='DB_',
        extra="ignore"
    )


postgres_settings = PostgresSettings()
