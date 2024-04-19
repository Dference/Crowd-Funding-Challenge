# Modules
import os
import csv

# Set Values
month = 0
total = 0
prof_loss = 0
greatest_inc = 0
greatest_dec = 0
changes = []
dates = []
greatest_inc_date = ""
greatest_dec_date = ""

# Set path for file
budg_csv = os.path.join("Resources", "budget_data.csv")

# Open the CSV file
with open(budg_csv) as csv_file:
   csvreader = csv.reader(csv_file, delimiter=",")

   # Read the header row first (skip this part if there is no header)
   csv_header = next(csvreader)

   # Find the total number of months and calculate total profit/loss
   for row in csvreader:
      month += 1
      total += int(row[1])

      # Profit/Losses Change
      current_profit = int(row[1])
      if month > 1:
            change = current_profit - previous_profit
            changes.append(change)
            dates.append(row[0])

            if change > greatest_inc:
               greatest_inc = change
               greatest_inc_date = row[0]
            elif change < greatest_dec:
               greatest_dec = change
               greatest_dec_date = row[0]

      previous_profit = current_profit

# Average Monthly Change
avg_monthly_change = sum(changes) / len(changes)
rounded_change = round(avg_monthly_change, 2)

# Export to text file
output_path = os.path.join("Analysis", "Findings.txt")
with open(output_path, "w") as textfile:
   textfile.write(f"Financial Analysis\n")
   textfile.write(f"______________________________________________\n")
   textfile.write(f"Total Months: {month}\n")
   textfile.write(f"Total: ${total}\n")
   textfile.write(f"Average Change: ${rounded_change}\n")
   textfile.write(f"Greatest Profit Increase: {greatest_inc_date} $({greatest_inc})\n")
   textfile.write(f"Greatest Profit Decrease: {greatest_dec_date} $({greatest_dec})\n")


# Print Totals
print(f"Total Months: {month}.")
print(f"Total: ${total}")
print(f"Average Change: {rounded_change}")
print(f"Greatest Profit Increase: {greatest_inc_date}, {(greatest_inc)}")
print(f"Greatest Profit Decrease: {greatest_dec_date}, {(greatest_dec)}")



















