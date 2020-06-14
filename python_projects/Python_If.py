

num1 = 12
key = False

if num1 == 12:
    if key:
        print('Num1 is equal to Twelve and they have the key!')
    else:
        print('Num1 is equal to Twelve and they do NOT have the key!')
elif num1 < 12:
    print('Num1 is less than Twelve!')
else:
    print('Num1 is NOT equal to Twelve!')
    


num2 = 2
sunny = False

if num2 == 4:
    if sunny:
        print('num2 is equal to 4 and it is Sunny outside')
    else:
        print ('num2 is equal to 4 and it is NOT Sunny outside')
elif num2 > 4:
    if sunny:
        print('num2 is greater than 4 and it is Sunny outside')
    else:
        print('num2 is greater than 4 and it is NOT Sunny outside')
else:
    print('Not enough, come back when you have 4 or more!')


num3=3

print(isinstance(num3,int))
