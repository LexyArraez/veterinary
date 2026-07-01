from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Aplication
    app_name: str
    app_version: str
    app_description: str
    database_url: str


    class Config:
        env_file = ".env"

    # Endpoint que nos va a permitir conectarnos a la base de datos
    # La string que construye la función
    # "postgresql://:postgres:qwerty@localhost:5432/vet_clinic"


settings = Settings()