portion_down_payment = float(25)/100
r = float(4)/100
goal_years = 3
goal_months = goal_years * 12
steps = 0
accuracy = 10000 # accuracy for how many decimals of accuracy we want our result 
upper_rate = accuracy # upper rate for bisection search
lower_rate = 0 # lower rate for bisection search
middle_rate = int((upper_rate + lower_rate) / 2) # middle rate for bisection search

# promt user for the values needed
annual_salary = float(input('Enter your annual salary: '))
semi_annual_raise = float(7)/100
total_cost = float(1000000)

# calculate down_payment value
down_payment = total_cost * portion_down_payment


def one_step(rate):
    "function for executing 1 step of bisection search"
    # these values are resetted each step
    current_savings = 0
    monthly_salary = annual_salary /12
    # find the savings in 36 months
    for months in range(goal_months):
        # add the semi annual raise to the monthly salary
        if months != 0 and months % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
        # savings increase by an interest from last month's savings  
        current_savings += current_savings * r /12 
        # savings increase by a portional of a month's salary
        current_savings += monthly_salary * float(rate) / accuracy
        
    # return the difference between savings and down payment
    return current_savings - down_payment


def sign(value):
    "function for finding the sign of a value"
    if value > 0:
        return 1
    elif value == 0:
        return 0
    elif value < 0:
        return -1

# we dont want the value but only the sign of the value to know which limit should be replace with middle
lower_sign = sign(one_step(lower_rate))
upper_sign = sign(one_step(upper_rate))
middle_sign = sign(one_step(middle_rate))

# after getting the initial sign for the 3 rates above, run the bisection search loop
while True:
    # this case ruins bisection search so we break out of the loop if this happens 
    if lower_sign == upper_sign:
        break
    # update steps
    steps += 1
    
    # if the range between upper_rate and lower_rate is < 2 
    # then we reached our desired accuracy
    if upper_rate - lower_rate < 2:
        break
    else:
        # if upper and middle rate have the same sign, update them and their sign values
        if middle_sign == upper_sign:
            upper_rate = middle_rate
            middle_rate = int((upper_rate + lower_rate) / 2)
            upper_sign = sign(one_step(upper_rate))
            middle_sign = sign(one_step(middle_rate))
        # if lower and middle rate have the same sign, update them and their sign values
        elif middle_sign == lower_sign:            
            lower_rate = middle_rate
            middle_rate = int((upper_rate + lower_rate) / 2)
            lower_sign = sign(one_step(lower_rate))
            middle_sign = sign(one_step(middle_rate))
    
    
# print the results if there are steps which meant bisection search was possible
if steps > 0:
    print('Best savings rate: ' + str(float(middle_rate)/accuracy))
    print('Steps in bisection search: ' + str(steps))
else: 
    print('It is not possible to pay the down payment in three years')