#Get file ready for import.
import os
import csv

#Set file to variable.
bank_file = os.path.join('../Resources/budget_data.csv')

#Making the lists
date_count = []
profits = []
month_count = []

count = 0
profits_total = 0
change_in_profits = 0
original_profits = 0


#Open CSV
with open (bank_file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)


    for row in csvreader:    
     
      count = count + 1 
        # Append date 
      date_count.append(row[0])

      # Append profits
      profits.append(row[1])

      # Sum of total profit 
      profits_total = profits_total + int(row[1])

      #Change in profits from month to month. 
      final_profit = int(row[1])
      month_count_profits = final_profit - original_profits

      month_count.append(month_count_profits)
      
      change_in_profits = change_in_profits + month_count_profits
      original_profits = final_profit

      #Calculate the average profit change.
      average_change_profits = (change_in_profits/count)

      # Find minimum and maximum change
      greatest_increase_profits = max(month_count)
      greatest_decrease_profits = min(month_count)

      #The dates at which minimum and maximum occurred. 
      increase_date = date_count[month_count.index(greatest_increase_profits)]
      decrease_date = date_count[month_count.index(greatest_decrease_profits)]

      # Print Results 

print("-----------------------------------------------------"),
print("Financial Analysis")
print("-----------------------------------------------------"),
print("Total Months: " + str(count)),
print("Total Profits: " + "$" + str(profits_total)),
print("Average Change: " + "$" + str(int(average_change_profits))),
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")"),
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")"),
print("-----------------------------------------------------")

      # Save analysis as txt file

with open('analysis.txt', 'w') as text:
    output = f"""\
-----------------------------------------------------
  Financial Analysis
-----------------------------------------------------

    Total Months: {count}
    Total Profits: ${profits_total}
    Average Change: ${int(average_change_profits)}
    Greatest Increase in Profits: {increase_date} (${greatest_increase_profits})
    Greatest Decrease in Profits: {decrease_date} (${greatest_decrease_profits})

-----------------------------------------------------
"""
    text.write(output)