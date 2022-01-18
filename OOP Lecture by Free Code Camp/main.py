from item import Item
from phone import Phone

'''
Check line - 63 to 65
Going to use the CSV file to do the following tasks :-
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
'''

Item.instantiate_from_csv()
item2 = Phone("samsung", 8000, 6, 2)
print(Item.all)

# print(Item.is_integer(2))
