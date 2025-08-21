shopping_list = []
def additem(item):
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list!")
def removeitem(item):
    if item in shopping_list:
       shopping_list.remove(item)
    else:
        print(f"{item} is not in the list")
def viewshop():
    if shopping_list:
        print("Shopping list:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("shopping list is empty acha ufala")
def clearshop():
    shopping_list.clear()
def main():
    while True:
        print("\n Chagua bois")
        print("1. Add to Shopping")
        print("2. Remove an item from shopping list")
        print("3. View/jionee")
        print("4. Clear shop")
        print("5. ishia")
        choice = input("Wanna skibidi shop or what? ")
        if choice == "1":
            item = input("addisia nini bois? ")
            additem(item)
        elif choice == "2":
            item = input("Toa kwa list nini buda? <uko broke kwani?> ")
            removeitem(item)
        elif choice == "3":
            viewshop()
        elif choice == "4":
            clearshop()
        elif choice == "5":
            print("\n Jidishi \nExiting the program.")
            break
        else:
            print("Invalid option, please try again.")
if __name__ == "__main__":
    main()        
        
        
        