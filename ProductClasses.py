"""
Alex Chaban
Due 02-19-2023
Prof. Ionut Cardei
COP4045
Problem 2: Product and DiscountedPrice Classes
"""

class Product:
    def __init__(self, name, mass, stock, cost):
        self.name = name
        self.mass = mass
        self.stock = stock
        self.cost = cost

    def __str__(self):
        return (f"{self.name}, ${self.cost}, {self.mass} kg, {self.stock} in stock")
    
    def price(self):
        return self.cost
    
    def set_price(self, ncost):
        self.cost = ncost
    

class DiscountedProduct:
    def __init__(self, discount, prod):
        self.discount = discount
        self.prod = prod

    def __str__(self):
        return (f"discounted {self.discount * 100}: {self.prod.name}, ${self.price()}, {self.prod.mass} kg, {self.prod.stock} in stock")
    
    def price(self):
        return self.prod.cost * (1 - self.discount)

def main():
    p = Product(name="Lavalamp", cost=30, mass=0.8, stock=123)
    print(p)
    disc_p = DiscountedProduct(0.2, p)
    print(disc_p.price()) 
    print(disc_p)
    p.set_price(20)
    print(p.price())
    print(disc_p) 

    q = Product(name="Graphic T-Shirts", cost=55, mass=0.42, stock=579)
    print(q)
    disc_q = DiscountedProduct(0.4, q)
    print(disc_q.price()) 
    print(disc_q)
    q.set_price(100)
    print(q.price())
    print(disc_q) 


main()