class Pizza:
    def __init__(self, topping):
        self.topping = topping

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples")
        else:
            return True


ingredients = ["chess", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)

# calling validate_topping method via class Pizza ingredients as input
print(Pizza.validate_topping(ingredients))
# calling validate_topping method via creating instance or object
print(pizza.validate_topping(ingredients))
