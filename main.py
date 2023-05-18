import random

from SQLQueries import *
from rental import Rental
import config


def generate_rentals_for_days():
    number_of_days_to_generate_data = int(sys.argv[1])
    current_date = fetch_last_rental_date()
    end_date = current_date + datetime.timedelta(days=number_of_days_to_generate_data)

    available_customers = fetch_all_customers_id()
    available_staff = fetch_all_staff_id()

    while current_date < end_date:
        available_cars = fetch_all_inventory_that_exist(current_date)

        rentals_to_generate = generate_rental_number(current_date)
        rentals_for_day = []

        for i in range(0, rentals_to_generate):
            if len(available_cars) == 0:
                continue
            if len(available_customers) == 0:
                available_customers = fetch_all_customers_id()
            if len(available_staff) == 0:
                available_staff = fetch_all_staff_id()

            rentals_for_day.append(
                create_random_rental(available_cars, available_customers, available_staff, current_date)
            )
        insert_executor(rentals_for_day)
        current_date += datetime.timedelta(days=1)


def generate_rental_number(current_date):
    if current_date.weekday() or current_date.month in config.high_season_months:
        return config.high_season_rental_number + random.randint(-5, 5)
    else:
        return config.base_rental_number + random.randint(-5, 5)


def create_random_rental(inventories, customers, staffs, date):
    customer = random.choice(customers)
    customers.remove(customer)

    inventory = random.choice(inventories)
    inventories.remove(inventory)

    staff = random.choice(staffs)
    rental_rate = fetch_car_rental_rate_by_id(inventory.car_id)

    rental_length = config.base_rental_length + random.randint(-5, 5)

    return Rental(None, rental_rate, customer.customer_id, inventory.inventory_id,
                  staff.staff_id, date, date + datetime.timedelta(days=rental_length), date, date)


if __name__ == '__main__':
    generate_rentals_for_days()
