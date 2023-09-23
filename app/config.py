from datetime import timedelta

from pydantic import RedisDsn
from pydantic_settings import BaseSettings


class MongoDsnSettings(BaseSettings):
    MG_PATH: str = "localhost"
    MG_PORT: str = "27017"
    MG_USER: str = "aboba"
    MG_PASS: str = "aboba"

    DATABASE_URL: str = f"mongodb://{MG_USER}:{MG_PASS}@{MG_PATH}:{MG_PORT}"

    class Config:
        env_file = ".env"
        extra = "ignore"


class RedisSettings(BaseSettings):
    REDIS_URL: RedisDsn = "redis://localhost:6379"

    class Config:
        env_file = ".env"
        extra = "ignore"


class ClientAPISettings(BaseSettings):
    APP_NAME: str = "jira"
    PATH_PREFIX: str = "/v1"
    APP_HOST: str = "http://0.0.0.0"
    APP_PORT: int = 8080
    AUTH_SECRET: str
    AUTH_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_SECONDS: int = timedelta(hours=1).seconds
    REFRESH_TOKEN_EXPIRE_SECONDS: int = timedelta(weeks=1).seconds

    SERVER_PORT: int = 8000
    SERVER_HOST: str = "0.0.0.0"

    class Config:
        env_file = ".env"
        extra = "ignore"


client_api_settings = ClientAPISettings()
mongo_settings = MongoDsnSettings(extra="ignore")
redis_settings = RedisSettings(extra="ignore")

# TODO: сделать получение настроек через DI
