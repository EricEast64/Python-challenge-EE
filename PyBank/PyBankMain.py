from datetime import date
import os
import csv

csv_path = os.path.join('Resources', 'budget_data.csv')

with open(csv_path, 'r') as budget_csv:
    csv_reader = csv.reader(budget_csv, delimiter=',')
    csv_header = next(csv_reader)
    
    month = []
    profit = []

    for row in csv_reader:
        month.append(row[0])
        profit.append(row[1])
    
    total_months = len(month)

    total_profit = len(profit)
    
    average_change = total_profit / total_months

    print(f"Total Months: {total_months}")
    print(f"Total Profit: {total_profit}")
    print(f"Average Change {average_change}")

    with open("PyBank.txt", "w") as f:
        f.write("OUTPUT")
   

    

    



        
