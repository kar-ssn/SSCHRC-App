import reflex as rx
from typing import Optional
from datetime import datetime


class Appointment(rx.Model, table=True):
    id: Optional[int] = None
    patient_id: int
    doctor: str
    date: datetime
    status: str