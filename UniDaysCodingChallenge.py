import math
class UnidaysDiscountChallenge:
    cart = {"A": 0,"B": 0,"C": 0,"D": 0,"E": 0}
    store_items = {"A": 8, "B": 12, "C": 4, "D": 7, "E": 5}

    def AddToBasket(self,item):
        self.cart[item] += 1

    def DisplayCart(self):
        print("Cart: ",self.cart)

    def DisplayStore(self):
        print("--Store--")
        for item in self.store_items:
            print(item, self.store_items[item])
        print("----")

    def Checkout(self):
        self.DisplayCart()
        cost = 0
        #Item Prices:
        cost += self.A() + self.B() + self.C() + self.D() + self.E()
        #Delivery Charge:
        print("Sub-total: ", cost)
        if cost < 50 and cost > 0:
            print("Shipping and Handling: 7")
            cost += 7
        else:
            print("Shipping and Handling: Free")
        print("Total: ", cost)

    def A(self):
        return self.store_items["A"] * self.cart["A"]

    def B(self):
        doubles = math.floor(self.cart["B"] / 2)
        remainder = self.cart["B"] % 2
        return doubles * 20 + remainder * self.store_items["B"]

    def C(self):
        triplets = math.floor(self.cart["C"] / 3)
        remainder = self.cart["C"] % 3
        return triplets * 10 + remainder * self.store_items["C"]

    def D(self):
        doubles = math.floor(self.cart["D"] / 2)
        remainder = self.cart["D"] % 2
        return (doubles + remainder) * self.store_items["D"]

    def E(self):
        triplets = math.floor(self.cart["E"] / 3)
        remainder = self.cart["E"] % 3
        return triplets * 10 + remainder * self.store_items["E"]

    def clear(self):
        for item in self.store_items:
            self.cart[item] = 0  


example = UnidaysDiscountChallenge()
example.DisplayCart()
example.DisplayStore()
choice = input("What would you like to add to your cart?  Comma separated for multiple items: ")
while (choice):
    if choice[0] in example.store_items:
        example.AddToBasket(choice[0])
        choice = choice[1:]
    else:
        print("Sorry ", choice[0], "is not a valid option")
        break
        
example.Checkout()

