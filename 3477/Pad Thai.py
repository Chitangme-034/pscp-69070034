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
    invalid = False
    for item in ingredients:
        if item not in allowed:
            invalid = True
    if invalid:
        print("This is not Pad Thai!!!")
    elif ingredients != allowed:
        print("This is bad!")
    elif flavors != required_flavors:
        print("Not Bad...")
    else:
        print("Delicious!")
main()
