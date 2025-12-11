from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_host: str
    db_port: int = 5432
    db_name: str
    db_user: str
    db_password: str

    db_pool_min = 1
    db_pool_max = 10

    class Config:
        env_file = ".env"
        env_file.encoding = 'utf-8'


settings = Settings()