from numpy import array

def activity_10():
    t_tuple = tuple(input("Enter numbers seperated by , : " ).split(","))

    for i in t_tuple:
        if int(i)%5 == 0:
            print(i)


