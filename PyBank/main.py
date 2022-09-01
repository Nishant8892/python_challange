
import os
import csv
os.chdir(os.path.dirname(__file__))
print("route of program is: " + os.getcwd())
csvpath = os.path.join('Resources', 'budget_data.csv')
total_months = []
total_profit = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header=next(csvreader)
    
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(row[1])

    total_number_of_months = len(total_months)
    
    total_profit = list(map(int, total_profit))
    net_total = sum(total_profit)
    
    average_change = net_total / total_number_of_months

    greatest_increase_amount = max(total_profit)
    total_increase_index = total_profit.index(greatest_increase_amount)
    greatest_increase_date = total_months[total_increase_index] 
    
    greatest_loss_amount = min(total_profit)
    total_loss_index = total_profit.index(greatest_loss_amount)
    greatest_loss_date = total_months[total_loss_index]


print_file = (f"  Financial Analysis \n"
      f"  ----------------------------\n"
      f"  Total Months: {total_number_of_months}\n"
      f"  Total: ${net_total}\n"
      f"  Average  Change: ${'{:.2f}'.format(average_change)}\n"
      f"  Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n"
      f"  Greatest Decrease in Profits: {greatest_loss_date} (${greatest_loss_amount})\n")

print(print_file)

output_file = os.path.join("output.txt")

with open('output.txt', 'w') as the_file:
    the_file.write(print_file)
    
