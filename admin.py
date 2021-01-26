import numpy
import machine
import cProfile

def menu():
    print("1. Add New coffee type")
    print("2. Update coffee details")
    print("3. Delete coffee details")
    print("4. Show coffee details")
    print("5. Update the raw materials:")
    print("6. Exit")
    print("_______________________________")
    try:
        x = int(input("Enter any step :"))

        if x == 1:
            add_new_coffee()
        elif x == 2:
            Update_Coffees()
        elif x == 3:
            delete_Coffee_Details()
        elif x == 4:
            coffees_details()
            menu()
        elif x == 5:
            update_stuff()
        elif x == 6:
            exit()
        else:
            print("Enter valid number")
            menu()
    except ValueError:
        print("Value Error")
        menu()



def add_new_coffee():
    try:

        name = input('Enter coffee name: ')
        price = input('Enter coffee price: ')
        origin = input('Enter coffee origin: ')
        mixtype= input('Enter coffee mix packets type: ')
        mixpacks = input('Enter quantity of mix packets: ')

        if mixpacks <= 20:
            point = machine.coffee(name, price, origin, mixtype, mixpacks)
            point. add_new_coffee()
        else:
            print("Your coffee mix packets out of limit")
    except:
        print("An Error")
    finally:
        menu()



def coffees_details():
    machine.display_coffees()


def Update_Coffees():
    coffees_details()

    try:
        userInId = int(input("Enter the modify ID :"))

        if  userInId < machine.siz_coffee_index():

            name = input('Enter coffee name: ')
            price = input('Enter coffee price: ')
            origin = input('Enter coffee Origin: ')
            mixtype = input('Enter type of coffee mix packets: ')
            mixpack = input('Enter quantity of coffee mix packets: ')

            machine.coffeeditails[userInId][0] = name
            machine.coffeeditails[userInId][1] = price
            machine.coffeeditails[userInId][2] = origin
            machine.coffeeditails[userInId][3] = mixtype
            machine.coffeeditails[userInId][4] = mixpack

            print("Coffee Modify Successfully")
        else:
            print("You Enter Coffee ID Do Not Excite")
            Update_Coffees()
    except ValueError:
        print("An exception occurred")
    finally:
        menu()


def delete_Coffee_Details():
    coffees_details()
    print("___________________________________")
    try:
        userInId = int(input("Enter the modify ID :"))
        if userInId < machine.siz_coffee_index():
            machine.cof = numpy.delete(machine.coffeeditails, userInId, axis=0)
            print("Coffee Delete Successfully")
        else:
            print("You Enter Coffee ID Do Not Excite")
            delete_Coffee_Details()
    except ValueError:
        print("An exception occurred")
    finally:
        menu()



def update_stuff():
    coffees_details()
    print("__________________________________")
    userInId = int(input("Enter the Update ID :"))
    if machine.coffeeditails[userInId][4] < 20:
        quantity = int(input('Enter quantity of packets: '))
        oldquantity = machine.coffeeditails[userInId][4] + quantity
        if oldquantity < 20:
            machine.coffeeditails[userInId][4] = oldquantity
            print("Update successfully")
        else:
            print("Stock overLoad")
    else:
        print("Stork Full")

menu()

