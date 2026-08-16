import json
import os
from pathlib import Path


path_patients = Path("materials/patients")

name_of_patient: str = input("Enter the full name of the patient separated by space (Ivanov Ivan Ivanovich): ")


name_of_patient = name_of_patient.lower().strip()
parts = name_of_patient.split(" ")

for i in range(len(parts)):
    parts[i] = parts[i].title()

patient_name_normalise = "_".join(parts)

folders = os.listdir(path_patients)

if patient_name_normalise in folders:
    path_to_card = path_patients / patient_name_normalise / "card.json"
    if path_to_card.exists():
        with open(path_to_card, "r", encoding="utf-8") as f:
            s = f.read()
        print(s)
    else:
        print("There is no patient card!")

else:
    print("There is no such patient!") 






