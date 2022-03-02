def intro_message():
    print(""" 

**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.   **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************   
    """)
 

intro_message()

order_list = []

menu = ['Wings', 'Cookies', 'Spring Rolls','Salmon','Steak','Meat Tornado','A Literal Garden','Ice Cream','Cake','Pie','Coffee','Tea','Unicorn Tears' ]

while True:
    
    order = input(">  " ).lower().title()
    
    if order in menu and order not in order_list:
            
        order_list.append(order)
        print(f'\n**  1 order of {order} have been added to your meal **\n')
          
    elif order in menu and order in order_list:

        order_list.append(order)
        count = order_list.count(order)
        print(f'\n** {count} orders of {order} have been added to your meal **\n')

    elif order == 'Quit':

        break

    elif order not in menu:

        print('\nplease choose one from the menu\n')
        

print('\nYour order is ' + ', '.join(order_list))

