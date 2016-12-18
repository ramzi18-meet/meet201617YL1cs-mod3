class Food:
    def __init__(self, customer_name , customer_plate , customer_time):
        self.name= customer_name
        self.plate=customer_plate
        self.time=customer_time

    def print_5(self):
        print('5')
    def details(self):
        print('The name of the user is ' + self.name)

customer1=Food('Jack' , 'Mashed Potatoes' , '10:30PM')
customer2=Food('George' , 'Mac and Cheese' , '7:00PM')
customer3=Food('John' , 'Regular Breakfast' , '9:20AM')

print(customer1.name, customer1.plate)

customer1.print_5()
customer3   .details()
