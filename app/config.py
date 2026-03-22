from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    user: str
    password: str
    host: str
    port: int
    name: str

    class Config:
        env_prefix = "SQL_DB_"

settings = Settings()

TORTOISE_ORM = {
    "connections": {
        "default": f"postgres://{settings.user}:{settings.password}@{settings.host}:{settings.port}/{settings.name}"
    },
    "apps": {
        "models": {
            "models": ["app.authentication.models", "app.files.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}