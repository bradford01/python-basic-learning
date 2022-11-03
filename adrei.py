
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        pass

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)
player3 =PlayerCharacter.adding_things(2, 3)
print(player3.name)


class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.dict = {
            "name": "yoyo",
            "has_pets": False
        }

    def __str__(self):
        return f"{self.color}"

    def __len__(self):
        return 5

    def __call__(self):
        return "yes??"
    def __getitem__(self, i):
        return self.dict[i]

    def __del__(self):
        print("deleted!")

action_figure =Toy("Blue", 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure["name"])




class user:
    def sign_in(self):
        print("logged in")


class  Wizard(user):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power {self.power}")

class Archer(user):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows


    def check_arrows(self):
        print(f"{self.arrows} remaining")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


Hb1 = HybridBorg("john", "shooting", 3)
print(Hb1.power)

