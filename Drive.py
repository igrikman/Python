class Car:
    name = None
    color = None
    speed = None

    def drive(self, speed):
        self.speed = speed
        u = speed
        try:
            if u < 60:
                while u != 60:
                    print(u, " km/h")
                    u += 1
            if u > 60:
                while u != 60:
                    print(u, " km/h")
                    u -= 1
            else:
                print(u, " km/h")
        except ValueError:
            print("ValueError in speed")

    def set_data(self, speed, name, color):
        self.speed = speed
        self.name = name
        self.color = color

    def get_data(self):
        print("Name ", self.name, " Color ", self.color, self.speed, " km/h")


car1 = Car()
car1.set_data(80, "BMV", "Black")
car1.get_data()
car1.drive(18)


car2 = Car()
car2.drive(50)