"""Exercise 9-3 Users"""

class User:
    """User class"""

    def __init__(self, first_name, last_name):
        """set initial values for User"""
        self.firstname = first_name
        self.lastname = last_name

    def describe_user(self):
        """print the user"""
        print(type(self), self.firstname, self.lastname)

    def greeting(self):
        """say hello to the user"""
        print("hello,", self.firstname, self.lastname)



class Admin(User):
    """Create special user with admin privileges"""

    def __init__(self, first_name, last_name, myprivileges):
        super().__init__(first_name, last_name)
        self.privileges = myprivileges

    def addprivileges(self,myprivileges):
        """add privileges to the admin user"""
        self.privileges += myprivileges

    def showprivileges(self):
        """display Admin's privileges"""
        print(self.privileges)
