from random import randint

class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
    
    def __str__(self):
        return "Ben - {}, %{}kadar tokum , {} param var, %{} kadar yemek var".format(
            self.name,
            self.fullness,
            self.house.money,
            self.house.food,
            )
    
    def eat(self):
        if self.house.food >= 10:
            print("{}, yedim ".format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            print("{}, yemek yok".format(self.name))
    
    def work(self):
        print("{} çalışıyor")
        self.house.money += 50
        self.fullness -= 10
    
    def play_game(self):
        print("Oyun oynadım")
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print("go to shop")
            self.house.money -= 50
            self.house.food += 50
        else:
            print("money nema")

    def go_in_the_house(self, house):
        self.house = house
        print("{} taşındı".format(self.name))
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            print("dead...")
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.play_game()


class House:
    def __init__(self):
        self.food = 10
        self.money = 50
    
    def __str__(self):
        print(self.food, "food,", self.money, "money")

usuri = Man(name="urus")
isuri = Man(name="suri")

adres1 = House()


usuri.go_in_the_house(adres1)
isuri.go_in_the_house(adres1)

for day in range(30):
    print("=" * 30, "Day{}".format(day), "=" * 30)
    isuri.act()
    print(isuri)
    usuri.act()
    print(usuri)

# print(isuri)
# isuri.eat()
# print(isuri)
# isuri.work()
# print(isuri)
# isuri.play_game()
# print(isuri)