import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    # Converting the following method into a class method.
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)  # Because .get() doesn't work with list.
            lines = list(reader)

        for i in lines:
            Item(
                name=i.get("Name"),
                price=float(i.get("Price")),
                quantity=int(i.get("Quantity"))
            )

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Making a list of all instances.
        Item.all.append(self)

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    # Making line-11 print better with 'represent' magic method.
    def __repr__(self):
        return f"Item - {self.name}, {self.price}, {self.quantity}"


'''
Gonna use the CSV file to do the following tasks :-
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
'''

Item.instantiate_from_csv()

print(Item.all)
