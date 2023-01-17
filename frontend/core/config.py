# dotenv_path = Path(".")

class Settings:
    PROJECT_NAME: str = "Universal Translator"
    PROJECT_VERSION: str = "0.0.2"
    TRANSLATION_URL: str = "localhost"
    TRANSLATION_PATH: str = "translate"
    TRANSLATION_PORT: int = 7890


settings = Settings()
