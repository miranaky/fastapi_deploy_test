from functools import lru_cache

from pydantic import BaseSettings


class Config(BaseSettings):
    app_name: str = "Fast API with MongoDB"
    mongo_db_path: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_config():
    return Config()
