import sys


def check_temp(t):
    if t < 15:
        return ("So cold!")
    elif t < 30:
        return ("It's a good day")
    elif t < 50:
        return ("it's hot...")
    else:
        return ("So hot!!")


if __name__ == '__main__':
    t = input("Current tempurature:")
    while t != 'q':
        t = int(t)

        print(check_temp(t))

        t = input("Enter new temperature:")

    sys.exit(0)
