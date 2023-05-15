import random

from SQLQueries import *

if __name__ == '__main__':
    base_rental_number = 30
    number_of_days_to_generate_data = int(sys.argv[1])
    last_date = fetch_last_rental_date()
    end_date = last_date + datetime.timedelta(days=number_of_days_to_generate_data)
    current_date = last_date

    while current_date <= end_date:
        print(current_date)
        current_date += datetime.timedelta(days=1)
        available_cars = fetch_all_inventory_that_exist2(last_date)
        available_customers = fetch_all_customer_that_exist_at_date(last_date)
        available_staff = fetch_all_staff()
        print(random.randint(-4, 4))

