from numpy import array



def activity_11():
    dict_fruit = {}
    have_more = True

    while have_more == True:
        fruit = input("Enter fruit name: ").upper()
        price = input("Enter it's price: ")

        dict_fruit[fruit] = price

        decision = input("have more fruits? Y/N ")
        if decision.upper() == 'N' :
            have_more= False

    seearch = input("Fruit to be searched: ").upper()

    if dict_fruit[seearch]:
        print("Fruit is avialable")
    else:
        print("fruit is not available")


	