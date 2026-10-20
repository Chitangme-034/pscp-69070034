"""Imposter"""
import json
def main():
    """Among Us"""
    members = {}
    while True:
        data = input()
        if data == "Start":
            break
        members.update(json.loads(data))
    dead = {}
    while True:
        name = input()
        if name == "End":
            break
        if name in members:
            dead[name] = members.pop(name)
    count = 0
    for role in members.values():
        if role == "Impostor":
            count += 1
    print(count, "Impostor Remains")
    print("***Alive***")
    for name in sorted(members):
        print(name, ":", members[name])
    print("***Dead***")
    for name in sorted(dead):
        print(name, ":", dead[name])
main()
