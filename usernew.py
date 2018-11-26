
class User():
    def __init__(self,first_name,last_name,group,path_profile):
        self.first_name = first_name
        self.last_name = last_name
        self.group = group
        self.path_profile = path_profile
        self.login_attempts = 0



    def describe_user(self):
        print("\nUser: " + self.first_name.title() +
        " " + self.last_name.title())
        print("Group: " + self.group.title())
        print("Path: " + self.path_profile)
        print("Login Attempts: " + str(self.login_attempts))

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " "
            + self.last_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1


    def reset_login_attempst(self,attempts):

        if self.login_attempts > attempts:
            self.login_attempts = 0



