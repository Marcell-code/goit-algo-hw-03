import random

    
def get_number_tickets(min_numb: int, max_numb: int, quantity: int):
    while True:
        try:
            if min_numb < max_numb and quantity >= 1 and quantity <= max_numb:      
                lucky_numbers = random.sample(range(min_numb, max_numb), quantity)
                lucky_numbers.sort()
                return lucky_numbers  
            else:
                return []    
        except ValueError:
            return []

print(get_number_tickets(1, 2, 5))
