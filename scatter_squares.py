import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]
# Построение граыфика с плавным возрастанием интенсивности цвета точек от значения по оси у
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)
# Назначение заголовка диаграммы и меток осей
plt.title("Square Numbers", fontsize=24)  # Подпись графика
plt.xlabel("value", fontsize=14)  # Подпись оси х
plt.ylabel('Square of Value', fontsize=14)  # Подпись оси у
# Назначение диапазона диаграммы и меток осей
plt.axis([0, 1100, 0, 1100000])
# Назначение размера шрифта делений на осях
plt.tick_params(axis='both', which='major', labelsize=14)
# Сохранение картинки графика( имя файла, отсекание пустых полей)
plt.savefig('imagies/squares_plot.jpg', bbox_inches='tight')
