import datetime
import sys

import mariadb

from model import Country, Address, Car, Equipment, Inventory, Store
from model import Customer
from model import Payment
from model import Rental
from model import Staff

try:
    conn = mariadb.connect(


    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()


def fetch_last_rental_date():
    cur.execute("SELECT * FROM rental ORDER BY rental_id DESC LIMIT 1")
    last_row: Rental = cur.fetchone()

    return datetime.date(2016, 1, 1) if last_row is None else last_row.rental_date


def fetch_all_countries():
    cur.execute("SELECT country_id, country FROM country")
    rows = cur.fetchall()

    countries = []
    for row in rows:
        print(*row)
        country_obj = Country(*row)
        countries.append(country_obj)

    return countries


def fetch_all_addresses():
    cur.execute("select * from address")
    rows = cur.fetchall()

    addresses = []
    for row in rows:
        print(*row)
        address_obj = Address(*row)
        addresses.append(address_obj)

    return addresses


def fetch_all_cars():
    cur.execute("select * from car")
    rows = cur.fetchall()

    cars = []
    for row in rows:
        print(*row)
        car_obj = Car(*row)
        cars.append(car_obj)

    return cars


def fetch_all_customer_that_exist_at_date(date):
    cur.execute("select * from customer WHERE create_date <= %s", (date,))
    rows = cur.fetchall()

    customers = []
    for row in rows:
        print(*row)
        customer_obj = Customer(*row)
        customers.append(customer_obj)

    return customers


def fetch_all_equipments():
    cur.execute("select * from equipment")
    rows = cur.fetchall()

    equipments = []
    for row in rows:
        print(*row)
        equipment_obj = Equipment(*row)
        equipments.append(equipment_obj)

    return equipments


def fetch_all_inventory_that_exist(date):
    cur.execute("SELECT inv FROM inventory AS inv WHERE create_date <= %s AND (last_update > %s OR sell_price IS NULL)",
                (date, date))
    rows = cur.fetchall()

    inventories = []
    for row in rows:
        print(*row)
        inventory_obj = Inventory(*row)
        inventories.append(inventory_obj)

    return inventories


def fetch_all_inventory_that_exist2(date):
    cur.execute('''SELECT i.inventory_id, i.car_id, i.production_year, i.fuel_type, i.store_id,
                    i.purchase_price, i.sell_price, i.create_date, i.last_update
                    FROM inventory i
                    LEFT JOIN (
                        SELECT inventory_id, MAX(rental_date) AS last_rental_date
                        FROM rental
                        GROUP BY inventory_id ) r 
                    ON i.inventory_id = r.inventory_id
                    WHERE i.create_date <= %s AND (i.last_update > %s OR i.sell_price IS NULL) 
                          AND (r.last_rental_date IS NULL OR i.last_update > r.last_rental_date)''', (date, date))
    rows = cur.fetchall()

    inventories = []
    for row in rows:
        print(*row)
        inventory_obj = Inventory(*row)
        inventories.append(inventory_obj)

    return inventories


def fetch_all_inventories():
    cur.execute("select * from inventory")
    rows = cur.fetchall()

    inventories = []
    for row in rows:
        print(*row)
        inventory_obj = Inventory(*row)
        inventories.append(inventory_obj)

    return inventories


def fetch_all_payments():
    cur.execute("select * from payment")
    rows = cur.fetchall()

    payments = []
    for row in rows:
        print(*row)
        payment_obj = Payment(*row)
        payments.append(payment_obj)

    return payments


def fetch_all_rentals():
    cur.execute("select * from rental")
    rows = cur.fetchall()

    rentals = []
    for row in rows:
        print(*row)
        rental_obj = Rental(*row)
        rentals.append(rental_obj)

    return rentals


def fetch_all_staff():
    cur.execute("select * from staff")
    rows = cur.fetchall()

    staffs = []
    for row in rows:
        print(*row)
        staff_obj = Staff(*row)
        staffs.append(staff_obj)

    return staffs


def fetch_all_stores():
    cur.execute("select * from store")
    rows = cur.fetchall()

    stores = []
    for row in rows:
        print(*row)
        store_obj = Store(*row)
        stores.append(store_obj)

    return stores


def get_staff_by_store():
    sql = '''
                SELECT  st.staff_id, st.first_name, st.last_name, st.store_id, st.address_id, st.email, st.manager_id, st.hired_date, st.last_update
                FROM store s
                JOIN staff st ON s.store_id = st.store_id
                ORDER BY s.store_id
            '''

    cur.execute(sql)

    results = cur.fetchall()

    staff_by_store = {}

    for row in results:
        print(*row)
        staff = Staff(*row)
        if staff.store_id not in staff_by_store:
            staff_by_store[staff.store_id] = []

        # Append the staff to the store's list
        staff_by_store[staff.store_id].append(staff)

    return staff_by_store
