#import packages
import os
import csv
import pandas as pd 

#create empty list
Months =[]
Profit = []
Loss = []
MonthLoss =[]
MonthProfit = []
TotalLoss = 0
TotalProfit = 0

#set path
csvpath = os.path.join(".", "budget_data.csv")

BudgetData = "budget_data.csv"

BudgetDataDf = pd.read_csv(BudgetData)

ProfitChange = BudgetDataDf.iloc[0, 1]

#open file 
with open(csvpath, newline="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    
    #loop through file
    for column in csvreader:  
        
        for row in csvreader:
            Months.append(row[0])
            #test- calculating profit changes
            ProfitChange = ProfitChange - int(row[1]) 
            print(ProfitChange)
            #create list for months of profit loss and net total profit and loss calculation
            if int(row[1]) < 0:
                Loss.append(int(row[1]))
                MonthLoss.append(row[0])
                TotalLoss = TotalLoss + int(row[1])
        
            elif int(row[1]) > 0: 
                Profit.append(int(row[1]))
                MonthProfit.append(row[0])
                TotalProfit = TotalProfit + int(row[1])
        
  
#create Profit loss dictionary with month as key 
MonthLossDict = dict(zip(MonthLoss, Loss))
MonthProfitDict = dict(zip(MonthProfit, Profit))
       

#Print number of Months In data set
print("Total no. of Months: %d"%(csvreader.line_num))

print(MonthLossDict)

#find greatest increase and decrease in profit

#print results
print(f"Total Profit is ${TotalProfit}")
print(f"Total Loss is ${TotalLoss}")
#write results to file
