'''
//Friend == SubClass
Contact == LeftSubclass
AddressHolder == RightSubclass
BaseClass == Contact
class Friend(Contact, AddressHolder):
     def __init__(self, name, email, phone, street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone
 '''


class BaseClass:
    num_base_calls = 0
    def call_me(self):
        print("Calling method on Base Class")
        self.num_base_calls += 1


class LeftSubclass(BaseClass):
    num_left_calls = 0
    def call_me(self):
        super().call_me() #now only calling the next method in class hierarchy
        print("Calling method on Left Subclass")
        self.num_left_calls += 1


class RightSubclass(BaseClass):
    num_right_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on Right Subclass")
        self.num_right_calls += 1


class Subclass(LeftSubclass, RightSubclass):
    num_sub_calls = 0
    def call_me(self):
        super().call_me()
        print("Calling method on Subclass")
        self.num_sub_calls += 1

s = Subclass()
print(s.call_me())
# Calling method on Base Class
# Calling method on Right Subclass
# Calling method on Left Subclass
# Calling method on Subclass
print(s.num_sub_calls, s.num_left_calls, s.num_right_calls, s.num_base_calls)