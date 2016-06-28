def start():
    print("Think of a number, any number. As long as it's between 1 and 100 (inclusive).")
    print()
    ready = input("Got it? (y/n)    ")
    if ready == "y":
        guessing()
    elif ready == "n":
        print("Oh, bye.")

def guessing():
    lo = 1
    hi = 100
    mid = (lo+hi)/2
    feedback = -2
    while feedback != 0:
        if feedback == -2:
            print("I guess", int(mid))
            feedback = int(input("Type -1, 0, or 1, depending on if my guess was lower, spot on, or higher than your number.    "))
        if feedback == 1:
            lo = lo
            hi = mid
            mid = int((lo+hi)/2)
            print("I guess", mid)
            feedback = int(input("Type -1, 0, or 1, depending on if my guess was lower, spot on, or higher than your number.    "))
        elif feedback == -1:
            lo = mid
            hi = hi
            mid = int((lo+hi)/2)
            print("I guess", mid)
            feedback = int(input("Type -1, 0, or 1, depending on if my guess was lower, spot on, or higher than your number.    "))
    if feedback == 0:
        print()
        print("I win! Thanks for playing. I mean losing.")

start()