import random

    
def get_number_tickets(min_numb, max_numb, quantity):
    if isinstance(min_numb, int) and isinstance(max_numb, int) and isinstance(quantity, int):       
        lucky_numbers = random.sample(range(min_numb, max_numb), quantity)
        lucky_numbers.sort()
        return f"Ваші щасливі номера {lucky_numbers}"
    else:
        return []

get_number_tickets(1, 49, 6)
print(get_number_tickets(1, 49, 6))
