from matplotlib import pyplot as plt
import numpy as np

def ADC_To_Voltage (volt_step):
    data_arr = np.loadtxt ('data.txt', dtype = int)
    volt_arr = data_arr * volt_step

    return volt_arr

def Time_Division (volt_arr, time_step):
    n_vals = volt_arr.size
    time_arr = np.linspace (0, n_vals * time_step, n_vals)
    
    return time_arr

with open ('settings.txt', 'r') as settings:
    tmp = [float(num) for num in settings.read().split("\n")]

time_step = 1 / tmp[0]
volt_step = tmp[1]

volt_arr = ADC_To_Voltage (volt_step)
time_arr = Time_Division (volt_arr, time_step)

plt.figure(figsize = (16, 10), dpi = 80)

plt.title ('Исследование зарядки и  разрядки конденсатора в RC-цепи', loc = 'center', fontsize = 24)

plt.xlabel('t, c', fontsize = 14)
plt.xlim(0, int(time_arr.max()) + 1)
plt.xticks(fontsize = 12, rotation = 30, ha = 'center', va = 'top') 

plt.ylabel('U, В', fontsize = 14)
plt.ylim(0, int(volt_arr.max()) + 0.5)
plt.yticks(fontsize = 12, rotation = 30, ha = 'right', va = 'top') 

plt.grid(color = 'black',                                      
        linewidth = 0.45,    
        linestyle = 'dotted')

plt.minorticks_on()

plt.grid(which='minor',
         color = 'grey',
         linewidth = 0.25,
         linestyle = 'dashed')

charge_time = 0
index = 0
while volt_arr[index] < volt_arr.max():
    charge_time += time_step
    index += 1

discharge_time = time_arr.max() - charge_time

plt.text(2 * time_arr.max() / 3, volt_arr.max() / 2 + 0.5, 'Время зарядки = %.2f с'   %charge_time,    fontsize = 14)
plt.text(2 * time_arr.max() / 3, volt_arr.max() / 2,   'Время разрядки = %.2f с'  %discharge_time, fontsize = 14)

plt.scatter(time_arr, volt_arr, s = 0.01, color = 'red')

plt.plot(time_arr, volt_arr, 'r', linewidth = 1, marker = "o", markevery = 200, label = 'Аппроксимирующая кривая', linestyle = '-')
plt.legend (loc = 'best', fontsize = 14)

plt.savefig ('Graph.png')
