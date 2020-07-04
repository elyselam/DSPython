class ContactList(list):
    def search(self,name):
        '''return all contacts that contain search val in their name'''
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts



class Contact:
    all_contacts = ContactList()
    '''part of class definition, shared by all instances. 
    there is only 1 Contact.all_contacts list. 
    be careful: if set self.all_contacts, you create a new instance variable with just that object
    the class variable is unchanged and accessible as Contact.all_contacts'''
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supplier(Contact):
    def order(self, order):
        print(f'you ordered {order} to {self.name}')




c = Contact('butt', 'butt@butts.com')
s = Supplier('sup', 'sup@sups.com')
print(c.all_contacts)

print(s.order("holes"))
print(type(s.order))


c1 = Contact("John A", "johna@example.net")
c2 = Contact("John B", "johnb@example.net")
c3 = Contact("Jenna C", "jennac@example.net")
print([c.name for c in Contact.all_contacts.search('John')])
# ['John A', 'John B']



class Friend(Contact):
    # def __init__(self, name, email, phone):
    #     self.name = name
    #     self.email = email
    #     self.phone = phone
    def __init__(self, name, email, phone):
        #returns the object as an instance of the parent class, allowing us to call the parent method directly:
        super().__init__(name,email)
        self.phone = phone


# mixin: superclass that's meant to be inherited by other class. add functionality to Contact class that allows sending email to self.email. it's a common task that other classes might want'''
class MailSender:
    def send_mail(self, message):


def inc(num, year):
    return (num*1.1)