price = float(input("Enter the price: "))

class Discount:
    def __init__(self, price):
        self.price = price
    
    def calculate_discount(self):
        discount_amount = 0.50 if self.price >= 2.00 else 0.25  
        return discount_amount
    
    def calculate_final_price(self):
        discount_amount = self.calculate_discount()
        final_price = self.price - discount_amount
        return final_price
    
def main():
    shop_discount = Discount(price)
    final_price = shop_discount.calculate_final_price()
    print(f"Final price: {final_price:.2f}€")

if __name__ == "__main__":
    main()
