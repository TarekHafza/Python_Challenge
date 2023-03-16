import os
import csv

csvpath = os.path.join("C:/Users/tarek/Documents/GitHub/Python_Challenge/PyBank/Resources/budget_data.csv")

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

with open(csvpath, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    for row in csvreader:
        dates.append(row[0]) 
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        total_months += 1
        total_pl = total_pl + int(row[1])

    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]
    avg_change = sum(profits)/len(profits)
    

print("Financial Analysis")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

output = open("output.txt", "w")
line1 = "Financial Analysis"
line2 = str(f"Total Months: {str(total_months)}")
line3 = str(f"Total: ${str(total_pl)}")
line4 = str(f"Average Change: ${str(round(avg_change,2))}")
line5 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line6 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6))