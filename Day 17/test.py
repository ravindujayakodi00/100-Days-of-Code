class User:
    pass


user1 = User()
user1.id = "001"
user1.username = "Ravindu"

print(user1.username)


class Car:
    def __init__(self, seats, doors):
        self.seats = seats
        self.doors = doors

car1 = Car(4, 2)

print(f"Car 1 has {car1.doors} doors")