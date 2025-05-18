import matplotlib.pyplot as plt
import datetime as dt


devices = {}

with open("data.csv", "r") as file:
    print(f'columns: {file.readline()}')

    lines = file.readlines()

    for line in lines:
       (timestamp,device_id,temperature,humidity,pressure) = line.strip().split(",")
       if devices.get(device_id):
           devices[device_id].append((timestamp,temperature,humidity,pressure))
       else:
           devices[device_id] = [(timestamp,temperature,humidity,pressure)]

colors = ["r", "b", "g"]
i = 0
for key, value in devices.items():
    x = []
    y = []
    for item in value:
        x.append( dt.datetime.strptime(item[0], "%Y-%m-%d %H:%M:%S") )
        y.append(float(item[1]))


    plt.plot(x, y, color=colors[i], label=key)

    i = i+1

plt.title("Devices") 
plt.xlabel("Timestamp") 
plt.ylabel("Temperature") 
           
plt.grid()
plt.show()