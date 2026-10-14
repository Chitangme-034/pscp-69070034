"""CuteCat CuteFox"""
def main():
    """Cats and Foxes"""
    num = int(input())
    cats = {}
    foxes = {}
    for _ in range(num):
        data = input().replace("{", "").replace("}", "")
        name, animal = data.replace('"', "").split(" : ")
        name = name.strip()
        animal = animal.strip()
        if animal.startswith("Cat"):
            cats[animal] = name
        elif animal.startswith("Fox"):
            foxes[animal] = name
    if "Cat01" not in cats and "Garfield" not in foxes.values():
        cats["Cat01"] = "Garfield"
    if "Fox01" not in foxes and "Fubuki" not in cats.values():
        foxes["Fox01"] = "Fubuki"
    print("Cat :", len(cats))
    print("Fox :", len(foxes))
    for animal in sorted(cats):
        print(cats[animal], ":", animal)
    for animal in sorted(foxes):
        print(foxes[animal], ":", animal)
main()
