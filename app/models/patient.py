import reflex as rx
from typing import Optional
from datetime import date


class Patient(rx.Model, table=True):
    id: Optional[int] = None
    user_id: int
    mrn: str
    dob: date
    contact_info: str