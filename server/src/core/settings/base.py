from pydantic import BaseSettings


class BaseAppSettings(BaseSettings):

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
