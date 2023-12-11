'''simplify the if else statement by this way for more readable and aesthetic'''

1def calc_time(grade):
    if grade >= 90: return 'A'
    if grade > 80 < 90: return 'B'
    if grade > 50 < 80: return 'C'
    return 'F'


print(calc_time(50))