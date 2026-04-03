from cinema.cinema.bar import CinemaBar
from cinema.cinema.hall import CinemaHall
from cinema.people.customer import Customer
from cinema.people.cinema_staff import Cleaner


def cinema_visit(
        customers: list,
        hall_number: int,
        cleaner: str,
        movie: str
) -> None:
    customer_instances = [Customer(c["name"], c["food"]) for c in customers]
    cleaning_staff = Cleaner(cleaner)
    cinema_hall = CinemaHall(hall_number)

    for customer in customer_instances:
        CinemaBar.sell_product(customer, customer.food)

    cinema_hall.movie_session(movie, customer_instances, cleaning_staff)
