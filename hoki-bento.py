addedMenu = {}
quantityA = 0
quantityB = 0

def mainMenu():
    print('\n' + '------- MAIN MENU -------')
    menuList = [ '1. menu', '2. cart', '3. checkout', '4. quit']
    for menu in menuList: 
        print(menu)

    choice = int(input('Select an option (1-4): '))

    if(choice == 1):
        print('\n' + '--------- MENU ---------')
        menuItem={}
        menuItem['1. Hoki packet A'] = 4
        menuItem['2. Hoki packet B'] = 6
        for key in menuItem:
            print(key + '  : $ ' + str(menuItem[key]['price']))
        
        chooseMenu = int(input('Which menu would you like to buy (1-2): '))
        print('Menu added!')

        if (chooseMenu == 1):
            addedMenu['Hoki packet A'] = 4
        else:
            addedMenu['Hoki packet B'] = 6

        mainMenu()
        
    elif(choice == 2):
        print('\n' + '---------- CART ----------')

        if(bool(addedMenu) == True):
            for key in addedMenu:
                print(key + '  : $ ' + str(addedMenu[key]))
        else:
            print('No menu has been added to cart')
        mainMenu()

    elif(choice == 3):
        def checkOut():
            price = 0
            print('\n' + '-------- CHECKOUT -------')
            if(bool(addedMenu) == True):
                for key in addedMenu:
                    print(key + '  : $ ' + str(addedMenu[key]))
                    price += int(addedMenu[key])
                print('TOTAL PRICE : $ ' + str(price) + '\n')

                pay = int(input('Insert payment: '))
                if (pay < price):
                    print('Not enough money')
                    checkOut()
                else:
                    print('Changes: $ ' + str(pay - price))
                    print('Thank you for shopping with us')
                    
                    addedMenu.clear()
            else:
                print('Empty checkout, please add the menu in to the cart first') 

            mainMenu()
        checkOut()

    else:
        return
mainMenu()