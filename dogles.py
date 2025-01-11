## declaring variables

import time
from itertools import repeat

restaurantName = str("Dogle's")
x = str('First course')
y = str('Sweets')
z = str('Drinks')

has_card_payment: bool = True
restaurant_balance: float = 100
client_cash_balance: float = 35.7
client_card_balance: float = 19
product_price: float = 25
client_bag: list[str]

menu_list1: list[str] = ['pizza', 'pasta', 'meat']
menu_list2: list[str] = ['ice cream', 'chocolate', 'cheesecake']
menu_list3: list[str] = ['cola', 'wine', 'water']

## the order application

print('========================================')
print('========================================')
print('          Welcome to', restaurantName, '!')
time.sleep(1)

print('   What would you like to order today?')
print('')
time.sleep(1)

print('First course:', menu_list1)
print('Sweets:', menu_list2)
print('Drinks:', menu_list3)
time.sleep(1)

print('')
print('Please type your answer:')
ordered_product = input('')

if (ordered_product not in menu_list1 + menu_list2 + menu_list3):
        print('Sorry, the ordered product is not available. :c')
        exit()
else:
        print(ordered_product.capitalize(), 'selected.')


time.sleep(1)
print('')
print('')
print('Balanca e vjeter e restorantit eshte:', restaurant_balance)
print('Balanca e vjeter e klientit eshte: cash', client_cash_balance,'leke, card:', client_card_balance, 'leke.')

time.sleep(1)
print('')
print('')
ans = input("Select your method of payment: (cash / card): ")


if (ans == "cash" and client_cash_balance >= product_price):
    print('')
    print("Proceed with payment")
    client_cash_balance = client_cash_balance - product_price
    restaurant_balance = restaurant_balance + product_price
    client_bag.append(ordered_product)


elif (ans == "card"):
    print("proceed with card")
    if (has_card_payment):
         if (client_card_balance >= product_price):
            print("proceed with payment")
            client_balance = client_card_balance - product_price
            restaurant_balance = restaurant_balance + product_price
            client_bag.append(ordered_product)
         else:
             print("Ju lutem kontrolloni limitin e kartes tuaj!")
    else:
        print("Ne nuk ofrojme pagesa me card!")


else:
    print("nuk e ofrojme kete lloje metode pagese...")
    exit(0)


print('The new balance of the restaurant is: ', restaurant_balance)
print('The new balance of the client is: cash: ', client_cash_balance, 'card: ', client_card_balance)
print('Client bag contains: ')
print(client_bag)

print('Thank you for choosing us!')