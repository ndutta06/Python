from numpy import array



def activity_7():
    new_list = []
    while len(new_list)<5:
        new_list.append(int(input("Enter a number: ")))

    sum_list = 0
    for n in new_list:
        sum_list += n
    print(sum_list)

	