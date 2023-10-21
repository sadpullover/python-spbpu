money_capital = 0  
salary = 5000  
spend = 6000  
increase = 3  
months = 10

required_savings = 0  

for _ in range(months):
    money_capital -= spend
    if money_capital < 0:
        required_savings += abs(money_capital)
        money_capital = 0
    spend += increase / 100 * spend

required_savings = round(required_savings)

print(required_savings
