import random
while True:
    try:
        min_numb = int(input("Введіть мінімальне значення: "))
        max_numb = int(input("Введіть максимальне значення: "))
        quantity = int(input("Введіть к-сть необхідних чисел: "))  

        if min_numb > max_numb:
            print("Мінімальне значення не може бути більше за максимальне спробуйте знову!")
            continue
        if quantity or min_numb or max_numb < 0:
            print("Числа не можуть бути відємними!")
            continue
        if quantity > max_numb - min_numb +1:
           print("У діапазоні замало чисел!")
           continue
        
        break 
    except ValueError:
        print("Ви ввели не правильні значення!")

def get_number_tickets(min_numb, max_numb, quantity):
    lucky_numbers = random.sample(range(min_numb, max_numb), quantity)
    lucky_numbers.sort()
    print(f"Ваші щасливі номера {lucky_numbers}")


get_number_tickets(min_numb, max_numb, quantity)