import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)  # Построение графика (x, y, толщина линии)
plt.title("Square Numbers", fontsize=24)  # Заголовок графика
plt.xlabel("Value", fontsize=14)  # Подпись оси х
plt.ylabel("Square of Values", fontsize=14)  # Подпись оси у
plt.tick_params(axis='both', labelsize=14)  # Оформление делений на осях
plt.show()  # Вывод графика
