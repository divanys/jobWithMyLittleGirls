# Даны два целых числа a и b (при этом a <= b, в случае, если условие ложно, сообщить об ошибке введённых данных).
# Выведите все числа от a до b включительн с шагом 2.


a = int(input("Введите значение a: "))
b = int(input("Введите значение b (b >= a): "))

if a > b:
    print("Ошибка: a должно быть меньше или равно b.")
else:
    for i in range(a, b + 1, 2):
        print(i)