import os 
import csv 
 
# Set path for file 
csvpath = os.path.join("budget_data.csv") 
 #using csv module to read data 
 
#Create Open Lists so the variables can be added and exported as Columns in a csv
Months = []
Total_Value = []
Avg_change = []
G_Increase = []
G_Decrease = [] 
Inc_date = []
Dec_date = []

#Open file
with open(csvpath) as csvfile: #csv reader specifies delimiter and variable that holds contents 
     csv_reader = csv.reader(csvfile, delimiter = ',')
     csv_header = next(csv_reader) #Reading the header row
     #print(f"{csv_header}") #This will print out the file headers if needed

     count = 0
     highest = 0
     lowest = 0
     value = 0
     pltotal = 0
     
#Total number of months
     for row in csv_reader: #loop through each row to determine values
          count += 1 #Running count of rows through the loop
          #The Net total amount of profit/loss over the period
          pltotal += int(row[1]) #Adding values in ProfitLoss Column
          value = int(row[1]) #Identifies the value of ProfitLoss Column
          #The greatest increase in those profits (date and amount)
          if(value > 0): #find the profits 
               if(value > highest): #compares each value to loops highest 
                    highest = value #sets this value to highest
                    highestdate = str(row[0]) #grabs the date for this value
          #The greatest decrease in those profiles (date and amount) 
          elif(value < 0): #find the losses
               if(value < lowest): #compares each value to loops lowest 
                    lowest = value #set this value to lowest
                    lowestdate = str(row[0]) #grabs the date for this value
          #The changes in profit/loss over period and then the averages of those changes
          average = int(round((pltotal / count),0)) #Average Profit or Loss for all rows
     #append to lists
     Months.append(count)
     Total_Value.append(pltotal)
     Avg_change.append(average)
     G_Increase.append(highest)
     Inc_date.append(highestdate)
     G_Decrease.append(lowest) 
     Dec_date.append(lowestdate)
     
     cleaned_csv = list(zip(Months,Total_Value,Avg_change,G_Increase,Inc_date,G_Decrease,Dec_date)) #create tuple for csv
 #Print to terminal    
     print(" ")#space
     print("Financial Analysis") #Title
     print(" ")#space
     print("-----------------------------------------------------") #title break
     print(" ")#space
     print(f"Total Months: {count}")
     print(" ")#space
     print(f"Total: {pltotal}")
     print(" ")#space
     print(f"Average Change: {average}")
     print(" ")#space
     print(f"Greatest Increase in Profits: {highestdate} ({highest}) ")
     print(" ")#space
     print(f"Greatest Decrease in Profits: {lowestdate} ({lowest}) ")
    
     

#Export to csv
output_file = os.path.join("Module3.csv")

with open(output_file, "w", newline = '') as datafile:
     writer = csv.writer(datafile)
     writer.writerow(["Months","Total_Value","Avg_change","G_Increase","Inc_date","G_Decrease","Dec_date"])
     writer.writerows(cleaned_csv)  


