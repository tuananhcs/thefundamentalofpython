class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return 3.14 * self.radius * self.radius

    def set_radius(self, new_radius):
        self.radius = new_radius

# Tạo một đối tượng Circle
circle = Circle(5)

# Truy cập và in ra bán kính ban đầu
print("Ban kính ban đầu:", circle.radius)

# Tính diện tích của hình tròn
print("Diện tích hình tròn:", circle.get_area())

# Thay đổi bán kính và in ra bán kính mới
circle.set_radius(7)
print("Ban kính mới:", circle.radius)

# Tính diện tích mới của hình tròn
print("Diện tích hình tròn mới:", circle.get_area())