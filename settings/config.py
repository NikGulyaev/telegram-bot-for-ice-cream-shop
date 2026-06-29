import os

from pydantic import SecretStr, PostgresDsn, Secret
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(os.path.dirname(__file__), ".envs/.env"))

    telegram_api_key: SecretStr
    LOG_LEVEL: str = "INFO"

    postgres_dsn: Secret[PostgresDsn]

    ADMIN_INTERFACE_PORT: int = 8001
    ADMIN_SECRET_KEY: SecretStr = SecretStr("secrtetkey")
    ADMIN_LOGIN: SecretStr = SecretStr("admin")
    ADMIN_PASSWORD: SecretStr = SecretStr("admin")
