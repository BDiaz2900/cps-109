import math
lead = int(input('Enter the lead to points: '))
possesion = input('Do the lead team have the ball (yes or no):')
seconds = int(input('Enter the number of seconds remaining: '))

calculation = lead - 3

if possesion == 'Yes' or 'yes':
    calculation += 0.5
else:
    calculations -= 0.5

result = calculation**2

percent_safe = (result/seconds) * 100

final_percent = round(percent_safe, 2)

if result > seconds:
    print(f'Lead is safe.')
    print(f'{final_percent} percent safe, {calculation} safety point margin')
else:
    print(f'Lead is NOT safe.')
    print(f'{final_percent}% percent safe, {calculation} safety point margin')