import datetime
from dataclasses import dataclass


@dataclass
class Payment:
    payment_id: int
    customer_id: int
    rental_id: int
    amount: float
    payment_date: datetime.date
    last_update: datetime.datetime


@dataclass
class Staff:
    staff_id: int
    first_name: str
    last_name: str
    store_id: int
    address_id: int
    email: str
    manager_id: int
    hired_date: datetime.date
    last_update: datetime.datetime


@dataclass
class Customer:
    customer_id: int
    first_name: str
    last_name: str
    address_id: int
    email: str
    birth_date: datetime.date
    create_date: datetime.datetime
    last_update: datetime.datetime


@dataclass
class Rental:
    rental_id: int
    rental_rate: float
    customer_id: int
    inventory_id: int
    staff_id: int
    rental_date: datetime.date
    return_date: datetime.date
    payment_deadline: datetime.date
    create_date: datetime.date


@dataclass
class Inventory:
    inventory_id: int
    car_id: int
    production_year: int
    fuel_type: str
    store_id: int
    purchase_price: float
    sell_price: float
    create_date: datetime.datetime
    last_update: datetime.datetime


@dataclass
class Equipment:
    equipment_id: int
    name: str
    type: str
    version: str
    create_date: datetime.datetime
    last_update: datetime.datetime


@dataclass
class InventoryEquipment:
    equipment_id: int
    inventory_id: int


@dataclass
class Car:
    car_id: int
    producer: str
    model: str
    rental_rate: float
    create_date: datetime.datetime
    last_update: datetime.datetime


@dataclass
class Store:
    store_id: int
    store_manager_id: int
    address_id: int
    last_update: datetime.datetime


@dataclass
class Address:
    address_id: int
    address: str
    address2: str
    city_id: int
    postal_code: str
    last_update: datetime.datetime


@dataclass
class City:
    city_id: int
    city: str
    country_id: int


@dataclass
class Country:
    country_id: int
    country: str
