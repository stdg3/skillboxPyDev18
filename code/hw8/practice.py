class Road:
    
    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class WareHouse:
    
    def __init__(self, name, content = 0):
        self.name = name
        self.content = content
        self.road_out = None
        self.queue_in = []
        self.queue_out = []

    def __str__(self):
        return "{} | cargo - {}".format(self.name, self.content)


    def set_road_out(self, road):
        """Road from warehouse"""
        self.road_out = road

    def truck_arrived(self, truck):
        self.queue_in.append(truck)
        truck.place = self
        print("{} arrived to warehouse {}".format(truck, self.name))

    def get_next_truck(self):
        if self.queue_in:
            truck = self.queue_in.pop()
            return truck

    def truck_ready(self, truck):
        self.queue_out.append(truck)
        print("{} is rady in warehouse {}".format(truck, self.name))

    def act(self):
        while self.queue_out:
            truck = self.queue_out.pop() # sondakini popla ve returnla (sil)
            truck.go_to(road=self.road_out)


class Vehicle:
    fuel_rate = 0
    total_fuel = 0

    def __init__(self, model):
        self.model = model
        self.fuel = 0

    def __str__(self):
        return "{} - model | fuel - {}".format(self.model, self.fuel)

    def tank_up(self):
        self.fuel += 1000
        Vehicle.total_fuel += 1000
        return "{} заправился".format(self.model)
    
    def act(self):
        if self.fuel <= 10:
            self.tank_up()
            return False
        return True
        

class Truck(Vehicle):
    fuel_rate = 50

    def __init__(self, model, body_space = 1000):
        super().__init__(model)
        self.body_space = body_space
        self.cargo = 0
        self.velocity = 100
        self.place = None
        self.distance_to_target = 0

    def __str__(self):
        res = super().__str__()
        return res + "| груз - {}".format(self.cargo)

    def ride(self):
        self.fuel -= self.fuel_rate
        if self.distance_to_target > self.velocity:
            self.distance_to_target -= self.velocity
            print("{} on road | to target {}".format(self.model, self.distance_to_target))
        else:
            print("{} arrived".format(self.model))
            self.place.end.truck_arrived(self)

    def go_to(self, road):
        self.place = road
        self.distance_to_target = road.distance 
        print("Model: {}".format(self.model))

    def act(self):
        if super().act():
            if isinstance(self.place, Road):
                self.ride()

class AutoLoader(Vehicle):
    """pogruschik"""

    fuel_rate = 30

    def __init__(self, model, bucket_capacity = 100, warehouse = None, role = "loader"):
        super().__init__(model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.truck = None

    def __str__(self):
        res = super().__str__()
        return res + " | loading - {}".format(self.truck)

    def act(self):
        if super().act(): 
            if self.truck is None:
                self.truck = self.warehouse.get_next_truck()
            elif self.role == "loader":
                self.load()
            else:
                self.unload()

    # загрузка - выгрузка 
    def load(self):
        if self.warehouse.content == 0:
            print("{} warehouse is empty".format(self.warehouse.name))
        self.fuel -= self.fuel_rate
        truck_cargo_rest = self.truck.body_space - self.truck.cargo
        if truck_cargo_rest >= self.bucket_capacity:
            self.warehouse.content -= self.bucket_capacity
            self.truck.cargo += self.bucket_capacity
        else:
            self.warehouse.content -= truck_cargo_rest
            self.truck.cargo += truck_cargo_rest
        
        if self.truck.cargo >= self.truck.body_space:
            self.warehouse.truck_ready(self.truck)
            self.truck = None
    
    def unload(self):
        self.fuel -= self.fuel_rate
        if self.truck.cargo >= self.bucket_capacity:
            self.truck.cargo -= self.bucket_capacity
            self.warehouse.content += self.bucket_capacity
        else:
            self.truck.cargo -= truck_cargo_rest
            self.warehouse.content -= self.truck.cargo
        
        if self.truck.cargo == 0:
            self.warehouse.truck_ready(self.truck)
            self.truck = None
            

TOTAL_CARGO = 100000

moscow = WareHouse(name = "MoscowWH", content= TOTAL_CARGO)

spb = WareHouse(name = "spb", content = 0)

msc_spb = Road(start = moscow, end = spb, distance = 715)
spb_msc = Road(start = spb, end = moscow, distance = 780)

moscow.set_road_out(msc_spb)
spb.set_road_out(spb_msc)

loader_1 = AutoLoader(model = "Cat", bucket_capacity = 1000, warehouse = moscow, role = "loader")
loader_2 = AutoLoader(model="Bobcat", bucket_capacity = 500, warehouse = spb, role = "unloader")

truck_1 = Truck(model="Kamaz", body_space=5000)
truck_2 = Truck(model="Belaz", body_space=2000)

moscow.truck_arrived(truck_1)
moscow.truck_arrived(truck_2)

hour = 0
while spb.content < TOTAL_CARGO:
    hour += 1
    print("-" * 30, hour, "-" * 30)
    truck_1.act()
    truck_2.act()

    loader_1.act()
    loader_2.act()

    moscow.act()
    spb.act()

    print("Truck 1 :", truck_1, "|", "Truck 2 :", truck_2)
    print("Loader 1 :", loader_1, "|", "Loader 2 :", loader_2)
    print("Moscow WH :", moscow, "|", "SPB WH :", spb)

print(Vehicle.total_fuel)
 