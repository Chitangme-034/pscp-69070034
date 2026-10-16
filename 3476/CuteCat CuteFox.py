"""CuteCat CuteFox"""
def main():
    """Cat & Foxes"""
    num = int(input())
    cats = {}
    foxes = {}
    for _ in range(num):
        data = input().replace("{", "").replace("}", "")
        name, code = data.replace('"', '').split(":")
        name = name.strip()
        code = code.strip()
        if code.startswith("Cat"):
            cats[code] = name
        elif code.startswith("Fox"):
            foxes[code] = name
    if "Cat01" not in cats and "Garfield" not in foxes.values() and "Garfield" not in cats.values():
        cats["Cat01"] = "Garfield"
    if "Fox01" not in foxes and "Fubuki" not in cats.values() and "Fubuki" not in foxes.values():
        foxes["Fox01"] = "Fubuki"
    print("Cat :", len(cats))
    print("Fox :", len(foxes))
    for code, name in sorted(cats.items(), key=lambda item: int(item[0][3:])):
        print(name, ":", code)
    for code, name in sorted(foxes.items(), key=lambda item: int(item[0][3:])):
        print(name, ":", code)
main()
