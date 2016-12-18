class UserAccount:
    def __init__(self , user_name , user_password , user_secret):
        self.name=user_name
        self.password=user_password
        self.secret=user_secret

    def print_my_name(self):
        print(self.name)

    def forgot_password(self, secret_try):
        if self.secret == secret_try:
            return self.password
        else:
            print('bad guess!')
        
        

user1=UserAccount('Ameer' , 'ameer1is2the3best4' , 'Was born in Ramallah')
user2=UserAccount('Subhi' , 'justincase221' , 'Hates Chinese Food')
user1.print_my_name()
print(user1.forgot_password( 'Was born in Ramallah'))


    
