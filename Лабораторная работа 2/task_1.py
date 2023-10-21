money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months_without_debts = 0

budget = salary + money_capital

while budget >= spend:
    budget += salary
    budget -= spend
    spend *= (1 + increase)
    months_without_debts += 1


print("Количество месяцев, которое можно протянуть без долгов:", months_without_debts)
