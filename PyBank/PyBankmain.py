#import packages
import os
import csv

#create empty list
Months =[]
ProfitList = []
Profit = []
Profit1 = 0
Loss = []
MonthLoss =[]
MonthProfit = []
TotalLoss = 0
TotalProfit = 0
ProfitChange = 0
ProfitChange1 = 0
GreatestIncrease = 0
GreatestDecrease = 0

#Create a first value for ProfitListChange, to keep dictionary acurate
ProfitChangeList = ['0']

#set input and output paths
csvpath = os.path.join(".", "budget_data.csv")
output_path = os.path.join(".", "new_budget_data.txt")

BudgetData = "budget_data.csv"

#open file 
with open(csvpath, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

    #save header and move to next line
    csv_header = next(csvfile)
    
    #loop through file
    for row in csvreader:  
        
        #Add to new list Month and Profit/loss
        Months.append(row[0])
        ProfitList.append(int(row[1]))
        Profit1 = int(row[1]) + Profit1
       
        #create list for months of profit loss and net total profit and loss calculation
        if int(row[1]) < 0:
            Loss.append(int(row[1]))
            MonthLoss.append(row[0])
            
            #calculate Total Loss
            TotalLoss = TotalLoss + int(row[1])
        
        elif int(row[1]) > 0: 
            Profit.append(int(row[1]))
            MonthProfit.append(row[0])

            #Calculate Total Gains 
            TotalProfit = TotalProfit + int(row[1]) 
 
    #iterate through ProfitList and find change values
    i = 1
    for x in range(85):
       
        ProfitChange1 = ProfitList[i] - ProfitList[i-1]
        ProfitChangeList.append(ProfitChange1)

        #find if decrease and update GreatestDecrease variable
        if ProfitChange1  < GreatestDecrease:
            GreatestDecrease = ProfitChange1 
            
        #find if increase and update GreatestIncrease variable
        elif ProfitChange1  > GreatestIncrease:
            GreatestIncrease = ProfitChange1
        
        ProfitChange = ProfitChange1
        i = i + 1 

#create Profit, loss, and Profit Change dictionaries with month as key - Might not need this, test mode
MonthLossDict = dict(zip(MonthLoss, Loss))
MonthProfitDict = dict(zip(MonthProfit, Profit))
ProfitChangeDict = dict(zip(ProfitChangeList, Months))

#Print number of Months In data set
print("Financial Analysis")
print("----------------------")
Average = round(ProfitChange / csvreader.line_num, 2)
print("Total Months: %d"%(csvreader.line_num))

#print results for Total Profit
print(f"Total Profit: ${Profit1}")

#Print Average Change
print(f"Average Change in Profit: ${Average}")

#Print greatest increase and decrease in profit
print(f"Greatest increase in profit: {ProfitChangeDict[GreatestIncrease]} ${GreatestIncrease}")
print(f"Greatest decrease in profit: {ProfitChangeDict[GreatestDecrease]} ${GreatestDecrease}")

#write results to file
with open(output_path, 'w', newline="") as text_file:
  
    print(f"Total Months: %d"%(csvreader.line_num), file=text_file )
    print(f"Total Profit $:{Profit1}", file=text_file)
    print(f"Average Change in Profit: ${Average}", file=text_file)
    print(f"Greatest increase in profit: {ProfitChangeDict[GreatestIncrease]} ${GreatestIncrease}", file=text_file)
    print(f"Greatest decrease in profit: {ProfitChangeDict[GreatestDecrease]} ${GreatestDecrease}", file=text_file)


