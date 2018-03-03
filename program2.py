time = int(input("Сколько времени?   "))
if time >= 1 and time <= 3:
           print("Сейчас ночь")
elif time >= 4 and time <= 11:
           print("Сейчас утро")
elif time == 12:
           print("Сейчас полдень")
elif time >= 13 and time <= 14:
           print("Сейчас обед")
elif time >= 15 and time <= 16:
           print("Сейчас день")
elif time >=17 and time <= 20:
           print("Сейчас вечер")
elif time >=21 and time <=23:
           print("Сейчас ночь")
elif time == 24:
           print("Сейчас полночь")
else:
           print("Введите число от 1 до 24")
