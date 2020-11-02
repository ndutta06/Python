from numpy import array

def activity_8():
    list_checker = list(input("Enter numbers seperated by , : " ).split(","))
    if list_checker[0] == list_checker[-1]:
        print("True")
    else:
        print("False")


