class User:

    def __init__(self, name):
        self.name = name


# create Objects
u1 = User("Farah")
u2 = User("Rube")

# The dictionary
users_db = {
    'id_u1': u1,
    'id_u2': u2
}

# Retrieve objects
print(users_db['id_u1'].name)  # Farah
