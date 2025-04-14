# Bien ben ngoai ham ben trong se thay duoc con nguoc lai thi khong


def outer_scope():
    name = 'Sam'
    city = 'New York'

    def inner_scope():
        print(f"Hello {name}, Greetings from {city}")

    return inner_scope()

