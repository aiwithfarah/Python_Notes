# Shopping List Manager: Create a program that allows a user to add items
#  to a list, remove items, and view the final list.
# Use a while loop to keep the program running until they choose to quit.

def shopping_list():

    shopping_items = []
    is_shopping = True

    while is_shopping:
        print("****MENU****")
        print("1. Add Item: ")
        print("2. Remove Item: ")
        print("3. View List: ")
        print("4. Quit")

        user_choice = input("Enter a choice between : 1,2,3,4: ")

        if user_choice == '1':
            item = input("Enter the item you want to add: ")
            shopping_items.append(item)

        elif user_choice == '2':
            item = input("Enter the item you want to remove?: ")
            if item not in shopping_items:
                print(
                    "You have not added this item to the list - hence ypu cannot remove it")
            else:
                shopping_items.remove(item)

        elif user_choice == '3':
            for _ in shopping_items:
                print(_)

        elif user_choice == '4':
            print("Thankyou so much for shoppin with us")
            is_shopping = False

        else:
            print("You have entered an incorrect option:    ")
    return shopping_items


x = shopping_list()
