"""Pad Thai"""
def main():
    """Ingredients"""
    allowed = {
        "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
        "Bean Sprouts", "Noodle", "Chives", "Lime", "Egg",
        "Oil", "Peanuts"
    }
    required_flavors = {"Sweet", "Sour", "Salty"}
    ingredients = set()
    flavors = set()
    while True:
        item = input()
        if item == "Cook":
            break
        ingredients.add(item)
    while True:
        flavor = input()
        if flavor == "End":
            break
        flavors.add(flavor)
    if not ingredients.issubset(allowed):
        print("This is not Pad Thai!!!")
    elif ingredients != allowed:
        print("This is bad!")
    elif flavors != required_flavors:
        print("Not Bad...")
    else:
        print("Delicious!")
main()
