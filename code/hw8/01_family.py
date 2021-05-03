# -*- coding: utf-8 -*-

# from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self, name = "home sweet home"):
        self.name = name
        self.money = 100
        self.food = 50
        self.dust = 0
        self.total_money_counter = 0
        self.total_food_counter = 0
        self.cat_food = 30
        self.total_cat_food_counter = 0
    
    def __str__(self):
        res = self.name + str(self.money) + "$" + " #" + str(self.food) +"=food"
        return res   
    

class Animate:    
    
    def __init__(self, name, fullness = 30, happiness = 100):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.home = None
        self.action = None

    def __str__(self):
        return "{}-{}, живу в {}".format(self.name, self.action, self.home)
    
    def go_in_the_house(self, home):
        self.home = home
        self.fullness -= 10

    def live_on(self):        
        home.dust += 5
        if self.home.dust >= 90:            
            self.happiness -= 10
        
        if (self.home.food <= 0 and self.fullness <= 0) or self.happiness <= 10:
            return False
        elif self.fullness > 0:
            return True


class Husband(Animate):

    def __init__(self, name):
        super().__init__(name)
        # self.prev_act_is_resting = True
        

    def __str__(self):
        res = super().__str__()
        return res + " | сыт на {}, счастлив на {}".format(self.fullness, self.happiness)

    def act(self):
        self.action = "rest"
        if self.live_on():
            # happ >10 and home.food > 0
            # a_rand = randint(1, 2)
            # self.prev_act_is_resting = True if a_rand == 1 else False
            if self.fullness <= 10:
                self.eat()
                
            # self.fullness -= 10
            elif self.home.money < 350:
                self.work()
            # elif self.prev_act_is_resting == True:
            #     self.work()
            #     self.prev_act_is_resting = False
            else:
                self.gaming()
                # self.prev_act_is_resting = True
        else:
            print("dead!")

    def eat(self):
        rint = randint(15, 30)
        if self.home.food >= rint:
            self.home.food -= rint
            self.fullness += rint
            self.happiness += rint
            self.action = "eating"
        else:
            self.fullness = self.home.food
            self.home.food = 0            
            self.action = "помиражки"

    def work(self):
        self.fullness -= 10
        self.home.money += 150
        self.action = "working"
        # self.happiness -= 20
        self.home.total_money_counter += 150

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        self.action = "gaming"


class Wife(Animate):

    def __init__(self, name):
        super().__init__(name)
        self.fur_coat_cost = 350
        self.fur_coat_counter = 0
        self.cleaning_counter = 0

    def __str__(self):
        res = super().__str__()
        return res + " | сыта на {}, счастлива на {}".format(self.fullness, self.happiness)

    def act(self):
        self.action = "rest"
        if self.live_on():
            # print(" wf live on true " * 1)
            if self.fullness <= 10:
                self.eat()
            elif self.home.dust >= 80:
                self.clean_house()       
            elif self.home.food <= 60:
                self.shopping()
            elif self.home.cat_food <= 20:
                self.cat_shopping()            
            
            
            elif self.home.money >= self.fur_coat_cost + 100:
                self.buy_fur_coat()
            # else:
            #     self.happiness += 20

    def eat(self):
        rint = randint(15, 30)
        if self.home.food >= rint:
            self.home.food -= rint
            self.fullness += rint
            self.happiness += rint
            self.action = "eating"
        else:
            self.fullness = self.home.food
            self.home.food = 0  
            self.action = "помиражки o.O" # ölii 

    def shopping(self):
        self.fullness -= 10
        self.happiness += 20
        self.action = "shoppping"
        if self.home.money >= 50:
            self.home.money -= 50
            self.home.food += 50
            self.home.total_food_counter += 50
        
        # elif 0 < self.home.money < 50:
        #     self.home.money -= self.home.money
        #     self.home.food += self.home.money
        # else:
        #     print("no money no honey") # gaç

    def cat_shopping(self):
        self.fullness -= 10
        self.happiness += 20
        self.action = "cat shopp"
        if self.home.money >= 50:
            self.home.money -= 50
            self.home.cat_food += 50
            self.home.total_cat_food_counter += 50

    def buy_fur_coat(self):
        self.fullness -= 10
        self.happiness += 60
        self.home.money -= self.fur_coat_cost
        self.fur_coat_counter += 1 

    def clean_house(self):
        self.fullness -= 10
        self.home.dust = 0
        self.happiness += 20
        print("house cleaned")
        self.cleaning_counter += 1


# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(home, color='cyan')

# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие ко
# водит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat(Animate):

    def __init__(self, name):
        super().__init__(name = name)

    def __str__(self):
        res = super().__str__()
        a = res + " | act:{}, happ{}, fullnes{}, catFood{}".format(self.action, self.happiness, self.fullness, self.home.cat_food)
        return a

    def act(self):
        if self.fullness <= 20:
            self.eat()
        else:
            self.fullness -= 10
            self.home.cat_food -= 10
            ch = randint(1,2)
            if ch == 1:
                self.sleep()
            elif ch == 2:
                self.soil()        

    def eat(self):
        self.fullness += 10
        self.happiness += 10 * 2
        self.action = "eating"

    def sleep(self):
        self.happiness += 5
        self.action = "sleepy"

    def soil(self):
        self.home.dust += 5
        self.action = "chiling"


home = House()
hsb = Husband(name='hsb')
wf = Wife(name='wf')

hsb.go_in_the_house(home)
wf.go_in_the_house(home)

murzik = Cat(name='Мурзик')
murzik.go_in_the_house(home)

# serge.gaming()
# serge.work()
# serge.eat()
for day in range(366):
    
    print("=" * 40, day,  "=" * 40)
    hsb.act()
    wf.act()
    murzik.act()
    print(hsb)
    print(wf)
    print(murzik)

print("now dust", hsb.home.dust)
print("total fur coat", wf.fur_coat_counter)
print("cleaned: ", wf.cleaning_counter)
print("total money ",home.total_money_counter)
print("total food  ",home.total_food_counter)
print("total cat food  ",home.total_cat_food_counter)



######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# # home = House()
# # serge = Husband(name='Сережа')
# # masha = Wife(name='Маша')
# # kolya = Child(name='Коля')
# # murzik = Cat(name='Мурзик')

# # for day in range(365):
# #     cprint('================== День {} =================='.format(day), color='red')
# #     serge.act()
# #     masha.act()
# #     kolya.act()
# #     murzik.act()
# #     cprint(serge, color='cyan')
# #     cprint(masha, color='cyan')
# #     cprint(kolya, color='cyan')
# #     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

