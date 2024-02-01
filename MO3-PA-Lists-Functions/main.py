# problem 7.4

things = ['mozzarella', 'cinderella', 'salmonella']

# problem 7.5

things[1] = things[1].capitalize() 
print(things)

# problem 7.6

things[0] = things[0].upper()
print(things)

# problem 7.7

things.remove('salmonella')
print(things)

# problem 9.1

def good():
    list = ['Harry', 'Ron', 'Hermione']
    return list

# problem 9.2

def get_odds(first=0, last=10, step=1):
    number=first
    while number < last:
        number += step
        if number % 3 == 0:
            yield number

# Call the function to get odds and print them
for odd_number in get_odds():
    print(odd_number)
        

