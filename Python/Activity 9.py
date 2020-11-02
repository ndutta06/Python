from numpy import array

def activity_9():
    input_1 = list(input("Enter numbers seperated by , : " ).split(","))
    input_2 = list(input("AGAIN Enter numbers seperated by , : " ).split(","))

    new_list = []

    for i in input_1:
        if (int(i) % 2) > 0:
            print(int(i) % 2)
            new_list.append(i)

    for j in input_2:
        if (int(j) % 2) == 0:
            new_list.append(j)

    print(new_list)


