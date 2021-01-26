import cProfile


class coffee:
    def __init__(self, name, price, orgin, mix, stock):
        self.name = name
        self.price = price
        self.origin = orgin
        self.mix = mix
        self.stock = stock

    def add_new_coffee(self):

        coffeeditails.append(
            [self.name, self.price, self.orgin, self.mix, self.stock])
        print("New coffee type added successfully")


coffeeditails = [["Latte", 250, "USA", "Milkkmix", 0],
                 ["Black Coffee", 200, "LK", "Blackcoffeemix", 10]]


def display_coffees():
    print("ID| CoffeeName | Price | Origin | Mix packets Type | Packets Quantity")

    for i in range(len(coffeeditails)):
        print(i, "|", coffeeditails[i][0], "|", coffeeditails[i][1], "|", coffeeditails[i][2], "|", coffeeditails[i][3], "|",
              coffeeditails[i][4])


def siz_coffee_index():
    return len(coffeeditails)

# cProfile.run('siz_coffee_index()')


def buy_coffee():
    try:
        show_Coffee_Details()
        userinput = int(input("Enter the coffee id :"))
        if userinput < siz_coffee_index():
            coines = int(input('Enter the coins: '))
            if coines > coffeeditails[userinput][1]:
                coffeeditails[userinput][4] = coffeeditails[userinput][4] - 1

                print("Take your remain {}".format(
                    coines - coffeeditails[userinput][1]))
                print("Enjoy !!!")
            else:
                print("Not enough money enter more coins:")

        else:
            print("Coffee id is dose not exit")
            buy_coffee()
    except ValueError:
        print("Value Error")

# cProfile.run('buy_coffee()')


def show_Coffee_Details():
    print("ID| Coffee Name | Price | Origin")

    for i in range(len(coffeeditails)):
        print(i, "|", coffeeditails[i][0], "|",
              coffeeditails[i][1], "|", coffeeditails[i][2])
#
# cProfile.run('show_Coffee_Details()')


def menu():
    print("\nWELCOME TO AUTOMATIC COFFEE MAKER  ")
    print("### CHOOSE ONE ####")
    print("\n1 : Buy a Coffee")
    print("2 : Show coffee details")
    print("3 : Exit")
    print("____________________________")

    try:
        step = int(input("Enter your step :"))

        if step == 1:
            buy_coffee()
        elif step == 2:
            show_Coffee_Details()
        elif step == 3:
            exit()
        else:
            print("Enter valid number")
            menu()
    except ValueError:
        print("An Error")
        menu()


menu()
