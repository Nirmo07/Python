
class MenuItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self):
        return f"{self.name}, Rs.{self.price:.2f}, Quantity: {self.quantity}"
