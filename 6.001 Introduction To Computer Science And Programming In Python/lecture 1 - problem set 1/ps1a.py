current_savings = 0
months = 0
portion_down_payment = float(25)/100
r = float(4)/100

# promt user for the values needed
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

# calculate down_payment value
down_payment = total_cost * portion_down_payment

# while the savings is still less than the down_payment, update the savings and months
while current_savings < down_payment:
    # savings increase by an interest from last month's savings  
    current_savings += current_savings * r /12 
    # savings increase by a portional of a month's salary
    current_savings += (annual_salary /12) * portion_saved
    # update month
    months += 1
    
# print the results
print('Number of months: ' + str(months))