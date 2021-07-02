
import os
import csv

#  Assigning some initial parameters

date=[]
profit_or_loss=[]
change=[]
delta=0
net_loss=0
net_profit=0
sum=0

#  Reading "budget_data.csv" file

csv_path=os.path.join("PyBank/budget_data.csv")

with open(csv_path,'r',newline='') as csvdata:
    csvreader=csv.reader(csvdata,delimiter=',')
    csvheader=next(csvreader)  #  Stores the header

#  Calculating the net total amount of profit/loss  

    for row in csvreader:
        date.append(row[0])
        profit_or_loss.append(int(row[1]))

# Indicating that positive & negative amounts are profit & loss,respectively.
        
        if int(row[1])<0:
            net_loss+=int(row[1])
        else:
            net_profit+=int(row[1])
        
        total_months=len(date)  #  Calculating the total number of months
    
        net_total_profit_loss=net_profit+net_loss
       
#  Calculating the average of changes in profit/loss 

    for i in range(len(profit_or_loss)-1):
        delta=profit_or_loss[i+1]-profit_or_loss[i]
        sum+=delta
        change.append(delta)
    average=round(sum/(len(profit_or_loss)-1),2)  
    
#  Assigning guess values for max/min changes in profit/loss

    max_profit=change[0]
    min_profit=change[0]
    date_max=date[1]
    date_min=date[1]

#  Calculateing the max/min changes in profit/loss 

    for i in range(len(change)):

        if min_profit>change[i]:
            min_profit=change[i]
            date_min=date[i+1]

        if max_profit<change[i]:
            max_profit=change[i]
            date_max=date[i+1]
            
#  Printing the results to the terminal

    print('---------------------------------------------------------')
    print("Financial Analysis")
    print('---------------------------------------------------------')
    print(f"Total Months: {total_months}")
    print(f"Total:   ${net_total_profit_loss}")
    print(f"Average Change: ${average}")
    print(f"Greatest Increase in Profits: {date_max}  (${max_profit})")
    print(f"Greatest Decrease in Profits: {date_min}  (${min_profit})")
    print('---------------------------------------------------------')

#  Exporting a text file with the results

csv_path=os.path.join("PyBank_result.csv")

with open(csv_path,'w',newline='') as result:
    csvwriter=csv.writer(result,delimiter=",")
    
    csvwriter.writerow(['Financial Analysis'])

    csvwriter.writerow(["---------------------"])
    
    csvwriter.writerow(['Total Months: ' + str(total_months)])
    
    csvwriter.writerow(['Total: $' + str(net_total_profit_loss)])
    
    csvwriter.writerow(['Average Change: $' + str(average)])

    csvwriter.writerow(['Greatest Increase in Profits: ' + str(date_max) + ' ($' + str(max_profit) + ')'])
    
    csvwriter.writerow(['Greatest Decrease in Profits: ' + str(date_min) + ' ($' + str(min_profit) + ')'])
