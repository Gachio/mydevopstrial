def ran_check(num, low, high):
    if num in range(low, high+1):
        print('{} is in the range between {} and {}'.format(num, low, high))
    else:
        print('The number is outside the range.')