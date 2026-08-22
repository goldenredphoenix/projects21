from pathlib import Path
from typing import Dict

from src.config_4 import Configuration


def main() -> Dict[str, str]:
    """Читает карточку врача и возвращает словарь."""

    # Шаг 1: создаём конфиг (читаем .env)
    config: Configuration = Configuration()

    # Шаг 2: строим путь к файлу
    file_path: Path = Path(config.base_folder) / "doctors" / f"{config.login}.txt"

    # Шаг 3: читаем файл
    content: str = file_path.read_text(encoding="utf-8")

    # Шаг 4: разбираем текст в словарь
    result: Dict[str, str] = {}
    for line in content.strip().split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()

    # Шаг 5: возвращаем словарь
    return result


if __name__ == "__main__":
    main()
    