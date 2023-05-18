import datetime
import sys
from functools import partial

import mariadb


def select_execute(cur, query: str):
    cur.execute(query)
    return cur.fetchall()


def insert_execute(cur, rentals):
    for rental in rentals:
        query = f''' INSERT INTO 
                    rental (rental_rate, customer_id, inventory_id, staff_id,
                            rental_date, return_date, payment_deadline, create_date) 
                    VALUES ({rental.rental_rate}, {rental.customer_id}, {rental.inventory_id}, {rental.staff_id},
                    '{rental.rental_date}', '{rental.return_date}', '{rental.payment_deadline}', '{rental.create_date}')
                '''
        cur.execute(query)


def create_cursor():
    try:
        conn = mariadb.connect(

        )
        conn.autocommit = True
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn.cursor(named_tuple=True)


select_executor = partial(select_execute, create_cursor())
insert_executor = partial(insert_execute, create_cursor())


def fetch_last_rental_date():
    last_row = select_executor("SELECT rental_date FROM rental ORDER BY rental_id DESC LIMIT 1")

    if not last_row:
        return datetime.date(2016, 1, 1)
    else:
        return last_row[0].rental_date + datetime.timedelta(days=1)


def fetch_car_rental_rate_by_id(car_id):
    return select_executor(f"select rental_rate from car where car_id= {car_id}")[0].rental_rate


def fetch_all_customers_id():
    return select_executor("select customer_id from customer")


def fetch_all_inventory_that_exist(date):
    query = f'''SELECT i.inventory_id, i.car_id
                    FROM inventory i
                    LEFT JOIN (
                        SELECT inventory_id, MAX(rental_date) AS last_rental_date
                        FROM rental
                        GROUP BY inventory_id ) r 
                    ON i.inventory_id = r.inventory_id
                    WHERE i.create_date <= "{date}" AND (i.last_update > "{date}" OR i.sell_price IS NULL) 
                          AND (r.last_rental_date IS NULL OR i.last_update > r.last_rental_date)'''

    return select_executor(query)


def fetch_all_rentals():
    return select_executor("select * from rental")


def fetch_all_staff_id():
    return select_executor("select staff_id from staff")
