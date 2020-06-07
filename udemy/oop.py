class Kettle(object):

    power_source = "electricity" #static fields
    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle("kenwood", 10)
kenwood.price = 20
print(kenwood.price)
print("model: {} = {}".format(kenwood.make, kenwood.price)) #model: kenwood = 20
print(kenwood.switch_on())
kenwood.switch_on()
print(kenwood.on)

print(Kettle.power_source)
print(kenwood.power_source)

print(kenwood.__dict__)
