#Biến private của class và chỉ get, set giá trị bằng hàm


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__odometer_reading = 0  # Biến private

    # Getter để lấy giá trị của odometer_reading
    def get_odometer_reading(self):
        return self.__odometer_reading

    # Setter để cập nhật giá trị của odometer_reading
    def set_odometer_reading(self, mileage):
        if mileage >= self.__odometer_reading:
            self.__odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

# Tạo một đối tượng Car
my_car = Car("Toyota", "Corolla", 2022)

# Đọc giá trị của odometer_reading thông qua getter
print(f"Odometer reading: {my_car.get_odometer_reading()}")

# Cập nhật giá trị của odometer_reading thông qua setter
my_car.set_odometer_reading(1000)

# Đọc lại giá trị của odometer_reading
print(f"Updated odometer reading: {my_car.get_odometer_reading()}")