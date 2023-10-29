money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

increase_coefficient = increase + 1
month_count = 0
while money_capital + salary - spend >= 0:
    money_capital += salary - spend
    spend *= increase_coefficient
    month_count += 1

# TODO Посчитайте количество месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", month_count)
