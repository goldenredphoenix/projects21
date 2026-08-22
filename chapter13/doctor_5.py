from pathlib import Path
from typing import Optional

from src.config_4 import Configuration


class Doctor:
    """Класс врача. Читает карточку и выписывает рецепты."""

    config: Configuration
    name: str
    speciality: str

    def __init__(self, config: Configuration) -> None:
        #  Сохраняем конфиг (запоминаем)
        self.config: Configuration = config             # self — это ссылка на сам объект. Без него Python не поймёт, к какому объекту ты обращаешься

        # строим путь к карточке
        file_path: Path = (
            Path(config.base_folder) / "doctors" / f"{config.login}.txt"
        )
        content: str = file_path.read_text(encoding="utf-8")

        # 3. Парсим карточку в словарь: содержимое файла -> словарь
        data: dict = {}
        for line in content.strip().split("\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()

        # 4. Заполняем атрибуты из карточки
        self.name: str = data.get("ФИО", "")
        self.speciality: str = data.get("Специальность", "")

        # инкапсуляция (снаружи нельзя записать файл минуя класс)
    def __write_receipt_to_file(self, recipe: str, filename: str) -> None:    #(два подчеркивания перед write - значит вызывает приватный метод, только внутри класса)
        """Записывает рецепт в файл в папку config.base_folder."""
        file_path: Path = Path(self.config.base_folder) / f"{filename}.txt"
        file_path.write_text(recipe, encoding="utf-8") #сздает файл и записывает в него текст

    def write_recipe(self, filename: Optional[str] = None) -> str:
        """Позволяет ввести рецепт и возвращает оформленный текст."""

        # 1. Приглашение ко вводу
        print("Enter recipe (to finish press Enter twice):")

        # 2. Многострочный ввод
        lines: list = []
        empty_count: int = 0

        while True:
            line: str = input()
            if line == "":
                empty_count += 1
                if empty_count == 2:
                    break          # 2 пустые строки подряд → СТОП
                lines.append(line)  # первую пустую строку добавляем
            else:
                empty_count = 0     # сбрасываем счётчик
                lines.append(line)

        # 3. Убираем последний пропуск строки
        if lines and lines[-1] == "":
            lines.pop()

        # 4. Склеиваем рецепт + ФИО + специальность
        recipe: str = "\n".join(lines)
        recipe += "\n\n" + self.name + "\n" + f"Doctor-{self.speciality}"

        # 5. Если передали имя файла — записываем
        if filename is not None:
            self.__write_receipt_to_file(recipe, filename)

        # 6. ВСЕГДА возвращаем рецепт
        return recipe
    