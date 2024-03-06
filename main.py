class Shoe:
    def __init__(self, brand, model, size, price):
        self.brand = brand
        self.model = model
        self.size = size
        self.price = price

    def display(self):
        return f"{self.brand} {self.model} Size: {self.size} Price: ฿{self.price}"

class TennisShoe(Shoe):
    def __init__(self, brand, model, size, price, court):
        super().__init__(brand, model, size, price)
        self.court = court

    def display(self):
        return f"{self.brand} {self.model} Size: {self.size} Court: {self.court} Price: ฿{self.price}"

shoe = Shoe("Nike", "Air Force 1 ", 8.5, 3400)
tennis_shoe = TennisShoe("Adidas", "Stan Smith", 6.5, 4000, "Clay")
def run():
    print(shoe.display())
    print(tennis_shoe.display())

if __name__ == '__main__':
    run()