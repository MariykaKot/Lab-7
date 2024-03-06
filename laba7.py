# Котуранова Мария Сергеевна 408879 R3135
# Вариант 9

#Задание 1
import numpy as np
import time
from matplotlib.animation import PillowWriter

# Создание двух списков и массивов NumPy
list1 = np.random.rand(1000000)
list2 = np.random.rand(1000000)
array1 = np.array(list1)
array2 = np.array(list2)

# Поэлементное перемножение списков
start_list = time.perf_counter()
result_list = [a * b for a, b in zip(list1, list2)]
end_list = time.perf_counter()
print(f"Время выполнения операции поэлементного перемножения стандартных списков: {end_list - start_list} секунд")

# Поэлементное перемножение массивов NumPy
start_array = time.perf_counter()
result_array = np.multiply(array1, array2)
end_array = time.perf_counter()
print(f"Время выполнения операции поэлементного перемножения массивов NumPy: {end_array - start_array} секунд")

#Задание 2
#Импорт библиотек
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#Задание списков для данных
time = []
angle = []
air_waste = []
#Извлечение данных из файла
with open('data1.csv', 'r') as f:
    for line in f:
        ind = line.split(sep=';')
        time.append(ind[0])
        angle.append(ind[9])
        air_waste.append(ind[15])
    f.close()

#Перенос названий из массивов данных
time_name = time[0]
time.pop(0)
time = np.array(time, float)
angle_name = angle[0]
angle.pop(0)
angle = np.array(angle, float)
air_waste_name = air_waste[0]
air_waste.pop(0)
air_waste = np.array(air_waste, float)


#Построение графиков от времени
plt.title('Угол опережения зажигания и расход воздуха в течение времени')
plt.xlabel(time_name)
plt.ylabel(angle_name +' и '+ air_waste_name)
plt.plot(np.array(time), np.array(angle))
plt.plot(np.array(time), np.array(air_waste))
plt.show()
#Построение графика корелляции
plt.title('График корреляции')
plt.xlabel(angle_name)
plt.ylabel(air_waste_name)
plt.plot(angle,air_waste,'o')
plt.show()

#Задание 3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5*np.pi, 5*np.pi, 100)
y = np.linspace(-5*np.pi, 5*np.pi, 100)
x, y = np.meshgrid(x, y)
z = y * np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

ax.set_title('Трехмерный график')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

#Дополнительное задание
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

figure = plt.figure()
l, = plt.plot([], [], 'k')

plt.xlim(-10, 10)
plt.ylim(-3, 3)

writer = PillowWriter(fps=30)

xlist = []
ylist = []

with writer.saving(figure, "sin.gif", 100):
    for xval in np.linspace(-10, 10, 100):
        xlist.append(xval)
        ylist.append(np.sin(xval))
        l.set_data(xlist,ylist)
        writer.grab_frame()
