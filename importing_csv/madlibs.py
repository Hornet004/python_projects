import csv

class item:

    #assign all empty objects
    all = []

    def __init__(self, name: str, price: float, quantity = 0):
        
        # assert the value of quantity recieved to avoid recieving negative values
        assert price >=0, f"price value {price} shouldn't be negative or less than 0"
        assert quantity >=0, f"Quantity value {quantity} shouldn't be negative or less than 0"
    
        self.name = name
        self.price = price
        self.quantity = quantity
        # append variables to object created
        item.all.append(self)
    
    def calculate_sum_total(self):
        return self.price * self.quantity
    
    @classmethod
    def instantiate_from_csv(cls):
         with open('madlibs\items.csv', 'r') as f:
              reader = csv.DictReader(f)
              items = list(reader)
              for item in items:
                   print(item)
    
    def __repr__(self):
            return f"('{self.name}, {self.price}, {self.quantity}')"


# item1 = item("Phone", 100, 1)
# item2 = item("Laptop", 1000, 3)
# item3 = item("Cable", 10, 5)
# item4 = item("Mouse", 50, 5)
# item5 = item("keyboard", 75, 5)

item.instantiate_from_csv()
