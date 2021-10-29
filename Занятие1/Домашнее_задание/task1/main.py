speed = int(input("Enter speed bytes per sec"))
tim = int(input("Enter time minutes"))  # Напишите ваше решение
coast = int(input("Enter final coast"))
a = speed * 60
b = a * tim // 1073741824
print(b)
print(coast * b - coast)
