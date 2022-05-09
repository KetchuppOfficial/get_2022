from matplotlib import pyplot as plt
import numpy as np

V_max = 3.3
levels = 2**8

def Get_Step ():
    with open ('settings.txt', 'r') as settings:
        tmp = [float(num) for num in settings.read().split("\n")]
    return tmp[1]

def ADC_To_Voltage ():
    data_arr = np.loadtxt ('data.txt', dtype = int)
    volt_arr = data_arr / levels * V_max

    return volt_arr

def Time_Division (volt_arr, time_step):
    n_vals = volt_arr.size
    time_arr = np.linspace (0, n_vals * time_step, n_vals)
    
    return time_arr

volt_arr = ADC_To_Voltage ()

time_step = Get_Step()
time_arr = Time_Division (volt_arr, time_step)

plt.figure(figsize = (16, 10), dpi = 80)

plt.title ('Исследование зарядки и  разрядки конденсатора в RC-цепи', loc = 'center', fontsize = 24)

plt.xlabel('t, c', fontsize = 14)
plt.xlim(0, (time_arr.size) * time_step)
plt.xticks(ticks = np.arange(0, time_arr.max(), time_step * 1000), fontsize = 12, rotation = 30, ha = 'center', va = 'top') 

plt.ylabel('U, В', fontsize = 14)
plt.ylim(0, V_max)
plt.yticks(ticks = np.arange(0, V_max, V_max / 15), fontsize = 12, rotation = 30, ha = 'right', va = 'top') 

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

plt.text(130, 1.5, 'Время зарядки = %.2f'   %charge_time,    fontsize = 14)
plt.text(130, 2,   'Время разрядки = %.2f'  %discharge_time, fontsize = 14)

plt.scatter(time_arr, volt_arr, s = 1, color = 'red')

plt.plot(time_arr, volt_arr, 'r', linewidth = 1, color = 'red', label = 'Аппроксимирующая кривая', linestyle = '-')
plt.legend (loc = 'best', fontsize = 14)

plt.savefig ('Try.png')
