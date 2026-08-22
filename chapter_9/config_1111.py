import os                       #читает переменные окружения
from pathlib import Path
from dotenv import load_dotenv


class Configuration:
    login: str         #подсказка, что тут будет строка
    base_folder: str

    def __init__(self) -> None:
        env_path: Path = Path(__file__).resolve().parent / ".env"       #resolve - делает путь полным, абсолютным; .parent - берет папку в которй лежит файл, env - добавляет имя файла
        load_dotenv(env_path)

        self.login: str = os.environ["LOGIN"]
        self.base_folder: str = os.environ["BASE_FOLDER"] 
