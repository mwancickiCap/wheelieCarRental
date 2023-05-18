import datetime
from dataclasses import dataclass


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
