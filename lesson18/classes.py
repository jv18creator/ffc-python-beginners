class Vehicle:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model

    def moves(self):
        return "vehicle moves..."

    def get_make_model(self):
        return f"I'm a {self.make} {self.model}"


my_vehicle = Vehicle("Tesla", "Model X")

print(my_vehicle.make)
print(my_vehicle.moves())
print(my_vehicle.get_make_model())

your_vehicle = Vehicle("Cadillac", "Escalade")
print(your_vehicle.get_make_model())


class Airplane(Vehicle):
    def __init__(self, make, model, faa_id) -> None:
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves_airplane(self):
        return self.moves()


class Truck(Vehicle):
    def moves(self):
        return "Rumbles along..."


class GolfCart(Vehicle):
    pass


cessna = Airplane("Cessna", "Skyhawk", 129)
mack = Truck("Mack", "Pinnacle")
golfwagon = GolfCart("Yamaha", "GC100")

print(cessna.moves_airplane())
print(cessna.get_make_model())

## polymorphism
print("\n\n")
for v in (my_vehicle, your_vehicle, cessna, mack, golfwagon):
    print(v.get_make_model())
    print(v.moves())
