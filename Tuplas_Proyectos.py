week = ("lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo")
profits = (13,30,35,20,47,46,15)

print(max(profits))
max_profit = max(profits)
max_profit_index = profits.index(max_profit)

max_profit_week = week[max_profit_index]
print("Pepe vendió "+ str(max_profit) + " helados"+ " el "+ str(max_profit_week)+ ". Ese día pudo comer con su familia...")

print(min(profits))
min_profit = min(profits)
min_profit_index = profits.index(min_profit)

min_profit_week = week[min_profit_index]
print("Pepe vendió "+ str(min_profit) + " helados"+ " el "+ str(min_profit_week)+ ". Ese día se quedó sin comer...")