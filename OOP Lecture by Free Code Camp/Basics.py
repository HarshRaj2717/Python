class Item:
    # Creating class attributes.
    # This is give to all instances and also class, can be changed for each instance at instance level separately.
    discount = 0.2  # 20% discount.

    def __init__(self, name: str, quantity: int, price: float):  # This is a magic method.
        # Run validations to the received arguments.
        assert price >= 0, "this string is give self-written assertion errors."
        assert quantity >= 0, f"{quantity} can not be negative."
        # Assign to self objects.
        self.name = name
        self.quantity = quantity
        self.price = price
        self.total_price = None
        self.total_discounted_price = None

    def calc_total_price(self):  # This is a method.
        self.total_price = self.quantity * self.price
        self.total_discounted_price = self.total_price - self.total_price * self.discount
        # Line-19 can also be written as following if class attributes don't need to be changed at instance level.
        self.total_discounted_price = self.total_price - self.total_price * Item.discount


# Creating an Instance
item1 = Item("Laptop", 100, 65000)
# item1.name = "phone"
# item1.quantity = 122
# item1.price = 10000

item1.calc_total_price()

print(item1.total_price)

print(Item.discount)
print(item1.discount)

# Magic attribute
print(Item.__dict__)  # All attributes for class level.
print(item1.__dict__)  # All attributes for instance level.
