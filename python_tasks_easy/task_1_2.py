# Задание 1_2
# Составьте программу подсчёта размера оплаты за электроэнергию по введенным значениям расхода электроэнергии и тарифа
# (тариф - строимость 1 кВт/ч)

consumption = float(input("Введите расход электроэнергии (в кВт/ч): "))
tariff = float(input("Введите тариф (стоимость 1 кВт/ч): "))

print(f"Сумма к оплате: {round(consumption * tariff, 2)} рублей")
