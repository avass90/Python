
def digit():
    x = input("Please input your age:")
    display(x)

def display(x):
    try:
        y = int(x) + 3
        print("{} + 3 = {}".format(x,y))
    except:
        print("You did not enter a number")
    finally:
        print("Whatever.... moving on....")





if __name__ == "__main__":
    digit()
