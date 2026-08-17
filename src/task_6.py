import csv
from tabulate import tabulate

path = "materials/schedule.csv" #запускать код из папки src, чтобы сработал путь

with open(path, mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    table = list(reader)

print(tabulate(
    table, 
    headers='keys', 
    tablefmt='github')
    )