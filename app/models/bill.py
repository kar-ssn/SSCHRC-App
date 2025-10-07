import reflex as rx
from typing import Optional
from datetime import date


class Bill(rx.Model, table=True):
    id: Optional[int] = None
    patient_id: int
    amount: float
    status: str
    due_date: date