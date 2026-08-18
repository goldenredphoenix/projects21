import json
import os
from pathlib import Path


path_patients = Path("materials/patients")

name_patients = input("Enter the full name of the patient separated by space (Ivanov Ivan Ivanovich): ")
name_patients = name_patients.lower().strip()
parts = name_patients.split(" ")

for i in range(len(parts)):
    parts[i] = parts[i].title()

patient_name_normalise = "_".join(parts)

folders = os.listdir(path_patients)

if patient_name_normalise in folders:
    path_to_card = path_patients / patient_name_normalise / "card.json"
    print(path_to_card)
    if path_to_card.exists():
        with open(path_to_card, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("There is no patient card!")

        surname = input("Enter the surname of the patient: ").strip().lower().title()
        name = input("Enter the name of the patient: ").strip().lower().title()
        patronymic = input("Enter the patronymic of the patient: ").strip().lower().title()
        birth = input("Enter the date of birth of the patient (1994-01-10): ").strip()
        sex = input("Enter the sex of the patient (M or W): ").strip().upper()

        d = {
                "Surname": surname,
                "Name": name,
                "Patronymic": patronymic,
                "Date of birth": birth,
                "Sex": sex
            }

        with open(path_to_card, "w", encoding="utf-8") as f:
            f.write(json.dumps(d, indent=4))
        with open(path_to_card, "r", encoding="utf-8") as f:
            print(f.read())

else: 
    print("There is no such patient!")

    