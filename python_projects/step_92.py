fname = "Daniel"
lname= "Christie"

print("Hello {} {}, welcome to Python".format(fname,lname))

x="Monday"
y="Friday"

print("{} is my least favorite day of the week, and {} is my favorite day of the week".format(x,y))

x = format( 14, 'x')
print(x)


def getSum(num1,num2):
    answer = num1 + num2
    print("The answer is {}.".format(answer))

myAdd = getSum

myAdd(2,2)

help()
