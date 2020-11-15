class Dog():
    def __init__(self,name,breed="Mutt",age="Unknown"):
        self.breed = breed
        self.name = name
        self.age = age

    def __str__(self):
        return "Hi: My name is {}. I'm aged {} and I'm a {}".format(self.name, self.age, self.breed)
    def __del__(self):
        print('User {} is removed'.format(self.name))

dachshund = Dog(breed='dachshund', name='Hot Dog')
print(dachshund)