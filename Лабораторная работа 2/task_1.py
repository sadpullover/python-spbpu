money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

months_without_debts = 0

budget = salary + money_capital

while budget >= spend:
    budget += salary
    budget -= spend
    spend *= (1 + increase)
    months_without_debts += 1

print("Можно протянуть без долгов", months_without_debts, "месяцев")
