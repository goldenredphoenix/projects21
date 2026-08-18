import csv
import os


first_app = input("Enter the time of the first appointment (08:00): ")
last_app = input("Enter the time of the last appointment (13:30): ")
one_app = input("Enter the duration of one appointment in minutes (15): ")
text_in_column = input("Enter the text that will be displayed in the column "Did the patient visit the doctor" by default (if you just press Enter, the default will be "No"): ")

def create_shedule(timestamps: list, default_value: str = 'No') -> list:
head = ['Time', 'Patient', 'Did the patient visit the doctor']

schedule = [header]
for time in timestamps:
        schedule.append([time, '', default_value])


current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir, 'schedule.csv')


with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(schedule)
    
return schedule  