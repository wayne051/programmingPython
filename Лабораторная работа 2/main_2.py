salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0
for i in range(months):
    money_capital += spend
    spend *= (1 + increase)

safety_net = money_capital - (salary * months)
safety_net = round(safety_net)



print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", {safety_net} ,"руб")
