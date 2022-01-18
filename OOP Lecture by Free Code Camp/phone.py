from item import Item


# This is a child class that inherits all functionality of its parent class 'Item' and can have additional options too.
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Calling super function to include __init__ of parent class in child class.
        super(Phone, self).__init__(
            name, price, quantity
        )

        # Run validations to the received arguments
        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

        # Making a list of all instances.
        Phone.all.append(self)  # Item class will also be updated.

        # Assign to self object
        # This broken_phones will not be for all of Item instances but only for Phone instances.
        self.broken_phones = broken_phones