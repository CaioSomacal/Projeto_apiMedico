from pydantic import BaseSettings

class Settings(BaseSettings):
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: str = "3306"
    MYSQL_DB: str = "agendamento_consultas"
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "sua_senha"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = ""
    REDIS_DB: int = 0

    class Config:
        env_file = ".env"

settings = Settings()
