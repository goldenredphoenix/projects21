# "import math


# # days = input("Enter the number of days in the course of treatment: ")
# # pills = 250
# # number_of_pack = 50

# # need_of_pack = math.ceil(int(days) / number_of_pack)
# # print(f"Need {need_of_pack} pack(s) of {number_of_pack} pills ({pills} mg) for the entire course of treatment")

# # # print("one" + val + "two")
# # print(f"one {val} two")
# # print("one {val} two".format(val=2))


# weight: str = input("Enter the weight of the patient: ")
# number_of_days = input("Enter the number of days in the course of treatment: ")

# weight: int = int(weight)
# PILL = 250
# NUMBER_IN_PACK = 50

# daily_dose = weight * 10
# single_dose = daily_dose / 2

# quantity = round(single_dose / PILL, 1)

# number_of_pack_for_pat = math.ceil(quantity / NUMBER_IN_PACK)

# print(f"Patient needs to take {quantity} pill(s) 2 times a day")
# print(f"Need {number_of_pack_for_pat} pack(s) of 50 pills (250 mg) for the entire course of treatment")"


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



