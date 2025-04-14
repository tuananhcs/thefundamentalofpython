class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it."

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# Tạo một instance (đối tượng) của lớp Car
my_car = Car("Toyota", "Corolla", 2022)

# Sử dụng các phương thức của đối tượng
print(my_car.get_descriptive_name()) # Output: 2022 Toyota Corolla

my_car.update_odometer(100)
print(my_car.read_odometer()) # Output: This car has 100 miles on it.

my_car.increment_odometer(50)
print(my_car.read_odometer()) # Output: This car has 150 miles on it.