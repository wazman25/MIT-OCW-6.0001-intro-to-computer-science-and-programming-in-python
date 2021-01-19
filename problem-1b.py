#!/usr/bin/env python# cost of the house
total_cost = float(input("What is the total cost of the home?"))

# down payment 
portion_down_payment = total_cost*.25
print(f"\n\nYour down payment will be {portion_down_payment}")

annual_salary = float(input("\nWhat is your annual salary?"))

portion_saved = float(input("\nwhat portion would you like to be saved?"))

monthly_savings = (annual_salary/12)*portion_saved

current_savings = 0.0
annual_return = 0.04
months=0
semi_annual_raise = float(input("\n\nWhat is your semi-annual raise in decimal?"))

#monthly_raise = (annual_salary/12) * semi_annual_raise 
#print(monthly_raise)

while current_savings < portion_down_payment:
  
  #make_each_month = 
  current_savings += (current_savings*annual_return)/12 + monthly_savings
  months+=1
  
  if months % 6 == 0:
    annual_salary += annual_salary * semi_annual_raise #+(annual_salary * semi_annual_raise)
    monthly_savings = (annual_salary / 12.0) * portion_saved
  

  

print(f"\n\nit will take {months} months to afford this downpayment")