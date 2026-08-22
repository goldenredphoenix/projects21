from typing import Optional

from src.config_4 import Configuration
from src.doctor_5 import Doctor


def main() -> str:
    """Основная логика: создаёт врача, спрашивает про сохранение, возвращает рецепт."""

    # 1. Создаём конфиг и врача
    config: Configuration = Configuration()      # (читает .env )
    doctor: Doctor = Doctor(config)              # читает карточку врача

    # 2. Спрашиваем: сохранять ли в файл?
    answer: str = input("Do I need to save the recipe to the file? ")

    # 3. Если ввели хоть что-то → спрашиваем имя файла
    filename: Optional[str] = None
    if answer:
        filename = input("Enter the name of the file where the recipe should be saved: ")

    # 4. Получаем рецепт
    recipe: str = doctor.write_recipe(filename)

    # 5. Возвращаем рецепт
    return recipe


if __name__ == "__main__":
    main()