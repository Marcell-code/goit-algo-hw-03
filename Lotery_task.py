import random

    
def get_numbers_ticket(min_numb: int, max_numb: int, quantity: int):
    for i in(min_numb, max_numb, quantity):
        if isinstance(i, bool) and not isinstance(i, int, float):
            return []
    if min_numb < 0:
        return []
    elif max_numb > 1000:
        return []
    elif quantity < 1 or quantity > (max_numb - min_numb + 1):
        return []
    else:
        lucky_numbers = random.sample(range(min_numb, max_numb), quantity)
        lucky_numbers.sort()
    return lucky_numbers  
             
        

print(get_number_tickets(1, 1200, 3))
