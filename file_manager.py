import csv
import shutil
import os
from src.expense import Expense

FILE_PATH = "data/expenses.csv"
BACKUP_DIR = "backup"

def save_expense(expense):
    with open(FILE_PATH, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(expense.to_list())

def load_expenses():
    expenses = []
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            expenses.append(Expense(row[2], row[1], row[0], row[3]))
    return expenses

def backup_data():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    shutil.copy(FILE_PATH, f"{BACKUP_DIR}/expenses_backup.csv")
