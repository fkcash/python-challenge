import os
import csv


PYBANK_CSV_PATH = os.path.join("Resources","budget_data.csv")


#Define lists
months = []
profit_loss_changes = []

#initialize variables
months_counter = 0
current_month_profit_loss = 0
previuos_month_profit_loss = 0
net_profit_loss = 0
profit_loss_change = 0


#print(os.getcwd())
os.chdir(os.path.dirname(os.path.realpath(__file__)))
#print(os.getcwd())



#Open and read csv file
with open(PYBANK_CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Read the header row first
    csv_header = next(csv_file)
    
        #Calculate the total number of months included in the dataset
    for row in csv_reader:
        months_counter = months_counter + 1

        #Calculate the net total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (months_counter == 1):
            # Make the value of previous month to be equal to current month
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # Compute change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[]
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes[]
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(months_counter - 1), 2)
    
    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {months_counter}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


    


  
