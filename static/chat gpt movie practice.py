class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_fullname(self):
        return f"{self._first_name} {self._last_name}".upper()


class Movie:
    def __init__(self, movie_type, quantity):
        self.movie_type = movie_type
        self.quantity = quantity

        if movie_type == 'Comedy':
            self.movie_cost = 5
        elif movie_type == 'Action':
            self.movie_cost = 4
        elif movie_type == 'Drama':
            self.movie_cost = 3


class Customer(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.movies_bought = []
        self.total_amount = 0


num_customers = int(input("Enter the number of customers: "))
customers = []

for i in range(num_customers):
    first_name = input("Enter customer's first name: ")
    last_name = input("Enter customer's last name: ")

    customer = Customer(first_name, last_name)

    num_comedy = int(input("Enter the number of Comedy movies: "))
    comedy_movie = Movie('Comedy', num_comedy)
    customer.movies_bought.append(comedy_movie)
    customer.total_amount += comedy_movie.quantity * comedy_movie.movie_cost

    num_action = int(input("Enter the number of Action movies: "))
    action_movie = Movie('Action', num_action)
    customer.movies_bought.append(action_movie)
    customer.total_amount += action_movie.quantity * action_movie.movie_cost

    num_drama = int(input("Enter the number of Drama movies: "))
    drama_movie = Movie('Drama', num_drama)
    customer.movies_bought.append(drama_movie)
    customer.total_amount += drama_movie.quantity * drama_movie.movie_cost

    customers.append(customer)

for customer in customers:
    print(customer.get_fullname())
    print(f"Comedy: ${customer.total_amount:.2f}")
    print(f"Action: ${customer.total_amount:.2f}")
    print(f"Drama: ${customer.total_amount:.2f}")
