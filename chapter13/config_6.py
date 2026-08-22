import os
from pathlib import Path
from dotenv import load_dotenv


class Configuration:
    """Конфигурация из задания 4. Читает LOGIN и BASE_FOLDER."""

    login: str
    base_folder: str

    def __init__(self) -> None:
        env_path: Path = Path(__file__).resolve().parent / ".env"
        load_dotenv(env_path)

        self.login: str = os.environ["LOGIN"]
        self.base_folder: str = os.environ["BASE_FOLDER"]


class SMTPSettings:
    """Настройки SMTP для отправки писем."""

    server: str
    port: int
    email: str
    email_password: str

    def __init__(self) -> None:
        env_path: Path = Path(__file__).resolve().parent / ".env"
        load_dotenv(env_path)

        self.server: str = os.environ["SMTP_SERVER"]
        self.port: int = int(os.environ["SMTP_PORT"])
        self.email: str = os.environ["SMTP_EMAIL"]
        self.email_password: str = os.environ["SMTP_EMAIL_PASSWORD"]