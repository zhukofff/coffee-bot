def get_amount_of_coffee():
    amount_of_coffee = int(input("""Сколько банок молотого кофе (100 г) вы покупаете в месяц?\n"""))
    return amount_of_coffee


def get_cost_of_ground_coffee():
    cost_of_ground_coffee = int(input("Введите цену за банку 100г помолотых кофейных зёрен:\n"))
    return cost_of_ground_coffee


def get_cost_of_coffee_machine():
    cost_of_coffee_machine = int(input("Введите цену кофемашины, которую планируете купить:\n"))
    return cost_of_coffee_machine


def calculation_count_of_zero_months():

    # data collection
    amount_of_coffee = get_amount_of_coffee()
    cost_of_coffee_jar = get_cost_of_ground_coffee()
    # if we want to drink quality coffee than we need buy a coffee machine
    # so this is the main question for i want to answer:
    # how long will the coffee machine pay off?
    cost_of_coffee_beans = get_cost_of_coffee_machine()
    cost_of_ground_coffee = 0
    count_of_months = 0

    while True:

        if cost_of_coffee_beans <= cost_of_ground_coffee:
            return print("Через {} месяц{} вы выйдете в 0 после покупки кофемолки.".format(count_of_months, ending_of_the_month(count_of_months)))

        cost_of_coffee_beans += 100 * amount_of_coffee
        cost_of_ground_coffee += cost_of_coffee_jar * amount_of_coffee
        count_of_months += 1


def ending_of_the_month(count_of_months):
    if count_of_months % 20 == 1:
        return
    elif (5 <= count_of_months % 20 <= 19) or count_of_months % 20 == 0:
        return "ев"
    else:
        return "а"


# so i can't find the best way to named variables i've created, therefore some remind what does they mean :
# 1) count of months when the equation goes to zero (count_of_ZERO_months)
# 2) count of months after reaching zero potential, i.e months when user will have some benefits (count_of_ZERO_PLUS_months)
def calculation_of_benefits(count_of_zero_months, count_of_zero_plus_months):
    return


while True:
    answer = input("Вы покупаете уже помолотые кофейные зёрна?\n")
    if answer == "Да" or answer == "да":

        print("""Мы верим, что вы сможете найти кофейные зёрна за цену 1г = 1р, поэтому все
        дальнейшие расчёты будут сделаны из этих значений.
        Считаем... Для вас! <3""")

        calculation_count_of_zero_months()
        break
    elif answer == "Нет" or answer == "нет":
        exit()
    else:
        print("Напишите Да / Нет. Нам нужные точные ответы, а вам нужны точные расчёты :)")
