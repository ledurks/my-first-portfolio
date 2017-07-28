class User:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.school = []
        self.gender = []
        self.city = []

    def num_age(self, age):
        self.age = age

    def school(self, school):
        self.school = school

    def gender(self, gender):
        self.gender = gender

    def city(self, city):
        self.city = city



class Network:
    # Define the fields and methods for your object here.
    def __init__(self):
        self.users = []
    # def add_user(self, user):



def main():
    # Define the program flow for your user interface here.
    first_name = input("first name:")
    person = User(first_name)
    print ("your first name has been entered as " + first_name)

    last_name = input("last name:")
    person = User(last_name)
    print ("your last name has successfully been enteres as " + last_name)

    age = input("age:")
    
# Runs your program.
if __name__ == '__main__':
    main()
