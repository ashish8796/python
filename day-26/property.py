# properties are created by putting the `porperty` decorator above a method,
# which means when the instance attribute with the same name as the method is accessed, the method will be called instead.
# use of setter/getter


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self.pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")


pizza = Pizza(["chesse", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True

print(pizza.pineapple_allowed)
