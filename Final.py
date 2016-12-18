class UserAccount:
    def __init__ (self, user_name , user_password , user_secret):
        self.name=user_name
        self.password=user_password
        self.secret=user_secret
    def print_my_name(self):
        print(self.name)
    def forgot_my_password(self , secret_attempt):
        if self.secret==secret_attempt:
            return self.password
        else:
            print("Wrong Answer as Orgiginally Submitted!")

user1=UserAccount('Ameer' , 'ameer1is2the3best4' , 'Was born in Ramallah')
user2=UserAccount('Subhi' , 'justincase221' , 'Hates Chinese Food')
user1.print_my_name()
print(user1.forgot_my_password('Was Born in Ramallah'))
