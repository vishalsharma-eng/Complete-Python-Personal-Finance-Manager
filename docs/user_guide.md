# User Guide – Python Personal Finance Manager

## 📌 Introduction
The Python Personal Finance Manager is a command-line based application that helps users
track daily expenses, analyze spending patterns, and generate financial reports.
This guide explains how to install, run, and use the application effectively.

---

## 🖥️ System Requirements
- Python 3.x installed on your system
- Any operating system (Windows / macOS / Linux)
- Basic knowledge of using the terminal or command prompt

---

## ⚙️ How to Run the Application

1. Open the terminal / command prompt
2. Navigate to the project directory:
   ```bash
   cd Python-Personal-Finance-Manager
Run the program:

bash
Copy code
python main.py
After running the command, the main menu will appear on the screen.

📋 Main Menu Options
pgsql
Copy code
1. Add New Expense
2. View All Expenses
3. View Category-wise Summary
4. Generate Monthly Report
5. Search Expenses
6. Backup Data
7. Exit

🔹 Menu Option Details

1️⃣ Add New Expense
Allows the user to add a new expense by entering:

Amount

Category (Food, Transport, Shopping, etc.)

Date (YYYY-MM-DD)

Description

The expense is saved permanently in a CSV file.


2️⃣ View All Expenses
Displays all recorded expenses in the following format:

javascript
Copy code
Date | Category | Amount | Description

3️⃣ View Category-wise Summary
Shows the total amount spent in each category.
Example:

makefile
Copy code
Food: ₹1500
Transport: ₹800

4️⃣ Generate Monthly Report
Generates a report for a specific month.
User needs to enter the month in:

Copy code
YYYY-MM
format (example: 2024-01).

5️⃣ Search Expenses
Allows searching expenses using keywords.
Search can be done by:

Category

Description

Example:

sql
Copy code
Enter search keyword: food

6️⃣ Backup Data
Creates a backup copy of the expense data file.
This helps prevent data loss.


7️⃣ Exit
Safely exits the application.

📂 Data Storage
All expense data is stored in:

bash
Copy code
data/expenses.csv
Data remains saved even after closing the program.

❗ Error Handling
The program validates numeric input for expense amounts

Prevents invalid menu selections

Displays helpful error messages for incorrect inputs

🔐 Best Practices
Enter correct date format (YYYY-MM-DD)

Backup data regularly

Do not delete the CSV file manually while the program is running

🔮 Future Enhancements
Graphical User Interface (GUI)

Budget planning feature

Data visualization (charts)

Export reports to Excel or PDF

📞 Support
This project is created for educational and internship purposes.
For improvements or issues, please refer to the project repository.

👤 Author
Vishal Kumar Sharma
