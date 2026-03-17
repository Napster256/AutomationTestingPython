from faker import Faker

generator = Faker()


def generate_user():
    return {
        "username": generator.first_name(),
        "email": generator.email(),
        "password": generator.password()
    }