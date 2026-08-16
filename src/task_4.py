import json
import os
from pathlib import Path

# создаем экземпляр класса для работы с путями 
path_patients = Path("materials/patients")

# получаем ФИО пациента из клавиатуры в формате NAME FAMILIY OTCHESTVO
name_of_patient: str = input("Enter the full name of the patient separated by space (Ivanov Ivan Ivanovich): ")

# приводим строку к нижнему регистру, убираем пробелы в начале и в конце строки
name_of_patient = name_of_patient.lower().strip()
parts = name_of_patient.split(" ")
parts = list(map(lambda x: x.title(), parts))
patient_name_normalise = "_".join(parts)

folders = os.listdir(path_patients)

if patient_name_normalise in folders:
    path_to_card = path_patients / patient_name_normalise / "card.json"
    if path_to_card.exists():
        with open(path_to_card, "r", encoding="utf-8") as f:
            s = f.read()
        print(s)
    else:
        print("Not fpond card")

else:
    print("Пациента нет") 






