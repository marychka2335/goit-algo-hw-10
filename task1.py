import pulp

model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

lemonade = pulp.LpVariable("lemonade", lowBound=0)  # Кількість "Лимонад" для виробництва
fruit_juice = pulp.LpVariable("fruit_juice", lowBound=0)  # Кількість "Фруктовий сік" для виробництва

model += (2 * lemonade + fruit_juice <= 100, "Обмеження_Води")  # Обмеження на "Вода"
model += (lemonade <= 50, "Обмеження_Цукру")  # Обмеження на "Цукор"
model += (lemonade <= 30, "Обмеження_Лимонного_Соку")  # Обмеження на "Лимонний сік"
model += (2 * fruit_juice <= 40, "Обмеження_Фруктового_Пюре")  # Обмеження на "Фруктове пюре"

model += lemonade + fruit_juice  # Максимізація загального виробництва

model.solve()

print(f"Статус: {pulp.LpStatus[model.status]}")  # Виведення статусу розв'язання
print(f"Лимонад: {pulp.value(lemonade)}")  # Виведення оптимальної кількості "Лимонад"
print(f"Фруктовий сік: {pulp.value(fruit_juice)}")  # Виведення оптимальної кількості "Фруктовий сік"
print(f"Загальна кількість продуктів: {pulp.value(model.objective)}")  # Виведення загального виробництва
