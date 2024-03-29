# Your task is to create a Python script that analyzes the records to calculate each of the following values:

# The total number of months included in the dataset

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

# Your analysis should align with the following results:

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import csv

# set the path for the csv file
budget_data_csv = "budget_data.csv"

# create variables to hold data
total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
profit_loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# read csv file
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skip header row
    next(csvreader)

    # need to loop through the rows within the csv file
    for row in csvreader:
        # question 1: count total number of months in dataset
        total_months += 1

        # question 2: the net total amount of profit/losses over the entire period
        total_profit_loss += int(row[1])

        # question 3: calculate the change in profit/losses between the current row and the previous row
        profit_loss_change = int(row[1]) - prev_profit_loss
        prev_profit_loss = int(row[1])

        # question 4: find the greatest increase in profits (date and amount) over the entire period
        if profit_loss_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_loss_change

        # question 5: find the greatest decrease in losses (date and amount) over the entire period
        if profit_loss_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_loss_change

# calculate the average change in profit/loss over the entire period
average_change = round(total_profit_loss / (total_months - 1), 2) #getting wrong average and can't figure out why???


# create or open a text file to write the results
with open("financial_analysis.txt", "w") as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_loss}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print("Results exported to 'financial_analysis.txt'")
