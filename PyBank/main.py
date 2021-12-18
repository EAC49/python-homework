#!/usr/bin/env python
# coding: utf-8

# In[2]:


from pathlib import Path
import csv


# In[3]:


filepath = Path("Resources/budget_data.csv")


# In[4]:


with open(filepath,"r") as file:
    budget_data = csv.reader(file,delimiter=',')
    header = next(budget_data)
    
    month = []
    pl = []
    
    print("Financial Analyses")
    print('------------------------------------------------')
    
    for row in budget_data:
        
        month.append(row[0])
        pl.append(row[1])
        
    print(f'Total Months: {len(month)}')
    
    sum_pl = 0
    
    for x in pl:

        sum_pl += int(x)
        
    print(f'Total: ${sum_pl}')

    
    delta = []
    total = 0
    
    for i in range(len(pl) - 1):
        
        net = int(pl[i+1]) - int(pl[i])
        
        delta.append(net)
        
    for m in delta:
        
        total += m
 
    ave_change = total / len(delta)
    
    print(f'Average Change: ${round(ave_change,2)}')
    
    
    largest = delta[0]
    
    for number in delta:
        
        if number > largest:
            
            largest = number
            
    date_increase_index = delta.index(largest)
    
    date_increase = month[date_increase_index + 1]
     
    print(f"Greatest Increase in Profits: {date_increase} $({largest})")
    
    
    smallest = delta[0]
    
    for number in delta:
        
        if number < smallest:
            
            smallest = number
            
    date_decrease_index = delta.index(smallest)
    
    date_decrease = month[date_decrease_index + 1]
     
    print(f"Greatest Decrease in Profits: {date_decrease} $({smallest})")


# In[40]:


#The total number of months included in the dataset.

#The net total amount of Profit/Losses over the entire period.

#The average of the changes in Profit/Losses over the entire period.

#The greatest increase in profits (date and amount) over the entire period.

#The greatest decrease in losses (date and amount) over the entire period.


# In[8]:


output_path = Path("financial_analyses.txt")
with open(output_path,"w") as f:
    f.write("Financial Analyses \n")
    f.write('------------------------------------------------ \n')
    f.write(f'Total Months: {len(month)}\n')
    f.write(f'Total: ${sum_pl} \n')
    f.write(f'Average Change: ${round(ave_change,2)} \n')
    f.write(f"Greatest Increase in Profits: {date_increase} $({largest}) \n")
    f.write(f"Greatest Decrease in Profits: {date_decrease} $({smallest}) \n")


# In[ ]:




